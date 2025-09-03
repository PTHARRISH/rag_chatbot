import asyncio
import os

import nest_asyncio
import streamlit as st
from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_community.document_loaders import (
    Docx2txtLoader,
    PyMuPDFLoader,
    TextLoader,
)
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

try:
    asyncio.get_running_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

nest_asyncio.apply()

# Configuration
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", google_api_key=api_key
)


# Streamlit APP
st.set_page_config(page_title="📂 RAG with Langchain", page_icon="H", layout="wide")
st.title("📂 RAG Application with Langchain")


upload_file = st.file_uploader(
    "Please Upload the file ......", type=[".pdf", ".docx", ".txt"]
)

if upload_file:
    with st.spinner("File uploading ..please wait for a moment"):
        temp_folder = "temp"
        os.makedirs(temp_folder, exist_ok=True)
        # Save file in the temp folder
        file_path = os.path.join(temp_folder, upload_file.name)
        with open(file_path, "wb") as f:
            f.write(upload_file.read())

        # Step 1:
        # Document loader
        # Extract the data from the Document
        if upload_file.name.endswith(".pdf"):
            loader = PyMuPDFLoader(file_path)
        elif upload_file.name.endswith(".docx"):
            loader = Docx2txtLoader(file_path)
        else:
            loader = TextLoader(file_path)

        docs = loader.load()

        # Step 2:
        # Text Splitting
        # Divide documents into chunks(500,50) second recursive will start
        # from last 50 of first recursive
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(docs)

        # Step 3:
        # embeddings and vector stores
        vectorstores = FAISS.from_documents(chunks, embeddings)
        retriever = vectorstores.as_retriever()

        # Step 4:
        # LLM Chain
        qa = RetrievalQA.from_chain_type(
            llm=llm, retriever=retriever, return_source_documents=True
        )
        st.success("File processed successfully!")

        # User Query
        user_query = st.text_input("User Input")

        if user_query:
            if st.button("Get Answer"):
                with st.spinner("Fetching answer... 🤔"):
                    response = qa(user_query)
                    st.subheader("💡 Answer")
                    st.write(response["result"])

                    st.subheader("📎 Sources / Metadata")

                    for i, docs in enumerate(response["source_documents"], 1):
                        st.markdown(f"**Source {i}: **{docs.metadata}")
                        st.write(docs.page_content[:200] + "....")
