from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def build_rag_chain():
    loader = TextLoader("data/knowledge_base.md")
    documents = loader.load()

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)

    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )
