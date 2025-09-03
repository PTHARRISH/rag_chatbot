# 📂 RAG Application with Langchain

A Retrieval-Augmented Generation (RAG) application built with Streamlit and Langchain, powered by Google's Gemini AI models. This application allows users to upload documents and interact with them through intelligent Q&A.

## 🌟 Features

- **Document Upload**: Support for PDF, DOCX, and TXT file formats
- **Smart Document Processing**: Automatic text extraction and processing
- **AI-Powered Q&A**: Chat with your documents using Google's Gemini 1.5 Flash model
- **Vector Embeddings**: Efficient document search using Google's embedding models
- **User-Friendly Interface**: Clean and intuitive Streamlit web interface

## 🚀 Technologies Used

- **Streamlit**: Web application framework
- **Langchain**: LLM application framework
- **Google Gemini AI**: Large language model (gemini-1.5-flash)
- **Google Generative AI Embeddings**: Document embedding model (embedding-001)
- **Python**: Programming language

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.7 or higher
- Google API key for Gemini AI
- Required Python packages (see Installation)

## 🛠️ Installation

1. **Clone the repository**
```
git clone https://github.com/PTHARRISH/rag_chatbot.git
cd rag-langchain-app
```

2. **Install required packages**
```
pip install streamlit langchain google-generativeai
```

3. **Set up your Google API key**
```
- Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- Set it as an environment variable or add it to your code
```
## 🔧 Usage

1. **Run the application**
```
streamlit run app.py
```

2. **Upload a document**
- Click on the file uploader
- Select a PDF, DOCX, or TXT file
- Wait for the file to be processed

3. **Start chatting**
- Ask questions about your uploaded document
- Get AI-powered answers based on the document content

## 📁 Project Structure
```
rag-langchain-app/
│
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── temp # Temporary uploaded files (auto-generated)
```

## 🔑 Environment Variables
```

Create a `.env` file in the root directory:

GOOGLE_API_KEY=your_google_api_key_here
```

## 📝 Code Overview

The application uses:
- `ChatGoogleGenerativeAI` for conversational AI capabilities
- `GoogleGenerativeAIEmbeddings` for document vectorization
- Streamlit for the web interface
- File handling for document processing


**Note**: This is a learning project created following a YouTube tutorial. Feel free to fork and enhance it further!
