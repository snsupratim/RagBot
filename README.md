# GROQ RAG ChatBot - Interact with Your PDFs

This project builds a **RAG (Retrieval-Augmented Generation)** based chatbot that allows you to **upload PDFs** and **chat with them**, using **GROQ LLM** and an **in-memory Chroma vector store**.

---

## Setup Instructions

### 1. Create a Virtual Environment

```bash
python -m venv myenv
```

Activate the environment:

- **On Windows**:

```bash
myenv\Scripts\activate
```

- **On macOS/Linux**:

```bash
source myenv/bin/activate
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

---

## Project Structure

```bash
groq_rag_chatbot/
|
├── index.py              # Main Streamlit app
├── requirements.txt      # Python dependencies
|
├── moduless/             # All modular logic
|   ├── pdf_handler.py        # PDF upload and loading logic
|   ├── vectorstore.py        # Chroma in-memory vector store setup
|   ├── llm.py                # GROQ LLM and RetrievalQA chain
|   ├── chat.py               # Chat interaction logic (input/output)
|   ├── chroma_inspector.py   # View vector store chunks from sidebar
```

---

## Features

- Upload and process multiple PDF files
- Store document embeddings in **Chroma** (in-memory)
- Query using **GROQ LLM** with **Retrieval-Augmented Generation (RAG)**
- Inspect vector store chunks from the sidebar
- Modular and clean code structure

---

> Build your own custom RAG ChatBot effortlessly! 🚀
