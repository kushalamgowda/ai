from langgraph.graph import StateGraph
from typing import TypedDict

from agent.intent import detect_intent
from agent.rag import build_rag_components

# Build RAG components
retriever, llm = build_rag_components()

class AgentState(TypedDict):
    input: str
    output: str


def agent_node(state: AgentState):
    user_message = state["input"]
    intent = detect_intent(user_message)

    if intent == "product_inquiry":
        docs = retriever.invoke(user_message)

        if not docs:
            return {"output": "I couldn't find relevant information. Let me connect you with sales."}

        context = "\n".join(d.page_content for d in docs)
        response = llm.invoke(
            f"Answer using context:\n{context}\n\nQuestion: {user_message}"
        )
        return {"output": response.content}

    if intent == "high_intent":
        return {"output": "Great! May I have your name?"}

    return {"output": "Hello! How can I help you with AutoStream today?"}


def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("agent", agent_node)
    graph.set_entry_point("agent")
    graph.set_finish_point("agent")
    return graph.compile()
