## Guide to Build the Best RAG Based ChatBot to interact with your PDFs:

1. Create a Virtual Environment:
   python -m venv myenv
   myenv/scripts/activate

2. Install Requirments:
   pip install -r requirements.txt

groq_rag_chatbot/
│
├── index.py # Main Streamlit app
├── requirements.txt # Python dependencies
│
├── moduless/ # All modular logic
│ ├── pdf_handler.py # PDF upload + loading logic
│ ├── vectorstore.py # Chroma in-memory vector store setup
│ ├── llm.py # GROQ LLM and RetrievalQA chain
│ ├── chat.py # Chat interaction logic (input/output)
│ ├── chroma_inspector.py # View vector store chunks from sidebar
