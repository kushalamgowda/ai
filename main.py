from dotenv import load_dotenv
load_dotenv()  
from agent.graph import build_graph


def main():
    graph = build_graph()

    print("🤖 AutoStream AI Agent (type 'exit' to quit)")

    state = {
        "input": "",
        "output": ""
    }

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Goodbye! 👋")
            break

        state["input"] = user_input
        state = graph.invoke(state)

        print("Agent:", state["output"])


if __name__ == "__main__":
    main()
