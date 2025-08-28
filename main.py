import streamlit as st
import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader,TextLoader,Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.vectorstores import FAISS,Pinecone
from langchain.chains import retrieval_qa

import asyncio
import nest_asyncio


try:
    asyncio.get_running_loop()
except RuntimeError:
    loop=asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

nest_asyncio.apply()

# Configuration
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

llm=ChatGoogleGenerativeAI(model='gemini-1.5-flash',google_api_key=api_key)
embeddings=GoogleGenerativeAIEmbeddings(model='models/embedding-001',google_api_key=api_key)


# Streamlit APP
st.set_page_config(page_title='RAG with Langchain',page_icon='H',layout='wide')
st.title("RAG Application with Langchain")


upload_file=st.file_uploader("Please Upload the file ......",type=[".pdf",".docx",''])