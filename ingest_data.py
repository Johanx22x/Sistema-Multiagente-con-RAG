from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter

loader = DirectoryLoader("./data/algebra_lineal_docs", glob="**/*.pdf", loader_cls=PyPDFLoader)
docs = loader.load()

if not docs:
    raise ValueError("⚠️ No se encontraron documentos PDF en la carpeta 'data/algebra_lineal_docs'.")

splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = splitter.split_documents(docs)

if not chunks:
    raise ValueError("⚠️ Los documentos están vacíos o no se pudieron dividir.")

embeddings = OllamaEmbeddings(model="mistral")
vectorstore = FAISS.from_documents(chunks, embeddings)
vectorstore.save_local("./vectorstore/faiss_index")

print("✅ ¡Base vectorial creada correctamente!")
