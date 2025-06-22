import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOllama

def get_rag_agent():
    db = FAISS.load_local("./vectorstore/faiss_index", OllamaEmbeddings(model="mistral"), allow_dangerous_deserialization=True)
    retriever = db.as_retriever()
    llm = ChatOllama(model="mistral")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
