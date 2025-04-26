import streamlit as st

def display_chat_history():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).markdown(msg["content"])

def handle_user_input(chain):
    user_input = st.chat_input("Pass your prompt here")
    if not user_input:
        return
    
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        result = chain({"query": user_input})
        response = result["result"]
        st.chat_message("assistant").markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    except Exception as e:
        st.error(f"Error: {str(e)}")

def download_chat_history():
    if st.session_state.get("messages"):
        content = "\n\n".join([f"{m['role'].upper()}: {m['content']}" for m in st.session_state.messages])
        st.download_button("💾 Download Chat History", content, file_name="chat_history.txt", mime="text/plain")
