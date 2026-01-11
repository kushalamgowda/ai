from agent.graph import build_graph

graph = build_graph()

state = {
    "messages": [],
    "intent": None,
    "name": None,
    "email": None,
    "platform": None
}

print("🤖 AutoStream AI Agent (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # Capture structured info manually
    if state["intent"] == "high_intent":
        if state["name"] is None:
            state["name"] = user_input
        elif state["email"] is None:
            state["email"] = user_input
        elif state["platform"] is None:
            state["platform"] = user_input
        else:
            state["messages"].append(user_input)
    else:
        state["messages"].append(user_input)

    state = graph.invoke(state)
    print("Agent:", state["messages"][-1])
