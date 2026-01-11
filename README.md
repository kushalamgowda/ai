
# 🤖 AutoStream AI Agent

A lightweight, intent-driven conversational AI agent built using **LangGraph**, **LangChain**, and **RAG (Retrieval-Augmented Generation)**. This project demonstrates how to route user queries based on intent and dynamically answer product-related questions using contextual documents.

---

## 📌 Features

* ✅ Intent detection (Greeting, Product Inquiry, High Intent)
* 🔀 LangGraph-based agent flow
* 📚 RAG using FAISS vector store
* 🧠 OpenAI-powered LLM (pluggable / mockable)
* 🧪 CLI-based interactive chat

---

## 🏗️ Architecture Overview

````
User Input
   ↓
Intent Detection
   ↓
LangGraph Router
   ├── Product Inquiry → RAG → LLM → Answer
   ├── High Intent     → Lead Capture
   └── General         → Greeting / Help


### Key Components

- **LangGraph** → Controls agent flow
- **LangChain** → LLM abstraction & tools
- **FAISS** → Vector database for document retrieval
- **OpenAI** → Chat & embeddings (optional for execution)

---

## 📁 Project Structure

````

ai/
│── main.py
│
├── agent/
│   ├── graph.py      # LangGraph flow
│   ├── intent.py     # Intent detection
│   ├── rag.py        # RAG pipeline
│
├── data/
│   └── knowledge_docs.md # Product info
│
├── requirements.txt
└── README.md

````

---

## ⚙️ Installation

### 1️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 OpenAI API Setup (Optional)

If you want **real AI responses**:

```bash
setx OPENAI_API_KEY "your_api_key_here"
```

>  If no API key or quota is available, the agent logic still works, but LLM calls must be mocked or skipped.

---

## ▶️ Run the Agent

```bash
python main.py
```

```
🤖 AutoStream AI Agent (type 'exit' to quit)

You: hello
Agent: Hello! How can I help you with AutoStream today?

You: How much does your product cost?
Agent: Great! May I have your name?

You: Kushi
Agent: Thanks Kushi! Our pricing depends on your use case...
You: ok
Agent: AutoStream pricing starts at ₹999/month with scalable plans.

You: exit
Agent: Goodbye! 👋
---

## 🧠 Intent Handling Logic

| Intent          | Action                  |
| --------------- | ----------------------- |
| Greeting        | Static welcome response |
| High Intent     | Collect user name       |
| Product Inquiry | RAG + LLM response      |

---

## 🧪 RAG Flow Explained

1. Load documents from `data/knowledge.txt`
2. Convert text → embeddings
3. Store vectors in FAISS
4. Retrieve relevant chunks
5. Answer using retrieved context

---

## 🚀 Why This Design?

* **LangGraph** enables scalable agent workflows
* **RAG** improves factual accuracy
* **Intent routing** reduces unnecessary LLM calls
* **Modular design** → production-ready

---

## 📌 Notes for Reviewers

* The project is intentionally **minimal but extensible**
* API usage is isolated for easy replacement
* Can scale to tools, memory, or multi-agent systems

---

## 🏁 Conclusion

This project demonstrates a clean, modern AI-agent architecture using industry-relevant tools. It balances clarity, modularity, and real-world applicability — suitable for internships, demos, and further extension.

---

👩‍💻 **Author**: Kushala Manjunath Gowda
