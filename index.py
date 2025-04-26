import warnings
import logging
import streamlit as st

# Local modules
from modules.chat import display_chat_history, handle_user_input, download_chat_history
from modules.pdf_handler import upload_pdfs
from modules.vectorstore import load_vectorstore
from modules.llm import get_llm_chain
from modules.chroma_inspector import inspect_chroma

# Silence noisy logs
warnings.filterwarnings("ignore")
logging.getLogger("transformers").setLevel(logging.ERROR)

st.set_page_config(
    page_title="RagBot!",     
)

# App title
st.title("Ask Ragbot! ")

# Step 1: Upload PDFs + wait for submit
uploaded_files, submitted = upload_pdfs()

# Step 2: If user clicks submit, update vectorstore
if submitted and uploaded_files:
    with st.spinner(" Updating vector database..."):
        vectorstore = load_vectorstore(uploaded_files)
        st.session_state.vectorstore = vectorstore


# Step 3: Display vectorstore inspector (Sidebar)
if "vectorstore" in st.session_state:
    inspect_chroma(st.session_state.vectorstore)

# Step 4: Display old chat messages
display_chat_history()

# Step 5: Handle new prompt input
if "vectorstore" in st.session_state:
    handle_user_input(get_llm_chain(st.session_state.vectorstore))

# Step 6: Chat history export
download_chat_history()
