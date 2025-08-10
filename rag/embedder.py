import json
import pandas as pd
from langchain.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

def load_documents():
    docs = []

    with open("data/Materials.json") as f:
        materials = json.load(f)
        docs.append(Document(page_content=json.dumps(materials), metadata={"source": "materials.json"}))

    df = pd.read_csv("data/price_template.csv")
    docs.append(Document(page_content=df.to_csv(index=False), metadata={"source": "price_template.csv"}))

    return docs

def create_vectorstore():
    documents = load_documents()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(documents=chunks, embedding=embeddings, persist_directory="chroma_db")
    vectordb.persist()
    return vectordb