from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

class Retrieval:
    def __init__(self, document: Document):
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        self.splits = text_splitter.split_documents([document])
        self.vectorstore = Chroma.from_documents(
            documents=self.splits,
            embedding=self.embeddings,
            persist_directory="./chroma_db"
        )
        self.retriever = self.vectorstore.as_retriever(search_kwargs={"k": 3})

    def ask_query(self, query: str, n_query: int) -> list:
        """Retrieve top-n relevant document chunks for the query."""
        self.retriever.search_kwargs["k"] = n_query
        docs = self.retriever.invoke(query)  # Query is embedded and used for similarity search
        return docs