from langgraph.graph import StateGraph, END
from agent.state import AgentState
from agent.intent import detect_intent
from agent.rag import build_rag_chain
from agent.tools import mock_lead_capture

rag_chain = build_rag_chain()

def process_message(state: AgentState):
    user_message = state["messages"][-1]
    intent = detect_intent(user_message)
    state["intent"] = intent

    if intent == "greeting":
        state["messages"].append("Hello! How can I help you with AutoStream today?")

    elif intent == "product_inquiry":
        answer = rag_chain.run(user_message)
        state["messages"].append(answer)

    elif intent == "high_intent":
        if not state.get("name"):
            state["messages"].append("Great! May I have your name?")
        elif not state.get("email"):
            state["messages"].append("Thanks! Could you share your email?")
        elif not state.get("platform"):
            state["messages"].append("Which creator platform do you use? (YouTube, Instagram, etc.)")
        else:
            mock_lead_capture(state["name"], state["email"], state["platform"])
            state["messages"].append("🎉 You're all set! Our team will contact you soon.")
            return END

    return state

def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("agent", process_message)
    graph.set_entry_point("agent")
    graph.add_edge("agent", END)
    return graph.compile()
