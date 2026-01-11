from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_core.embeddings import Embeddings
import numpy as np

# ---- MOCK EMBEDDINGS (NO API CALLS) ----
class MockEmbeddings(Embeddings):
    def embed_documents(self, texts):
        return [np.random.rand(384).tolist() for _ in texts]

    def embed_query(self, text):
        return np.random.rand(384).tolist()


def build_rag_components():
    loader = TextLoader("data/knowledge_base.md")
    documents = loader.load()

    embeddings = MockEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)

    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    return retriever, llm
