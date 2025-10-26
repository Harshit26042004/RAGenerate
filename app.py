import json
import os
import warnings
import streamlit as st
from streamlit_lottie import st_lottie, st_lottie_spinner
from tutor_rag.reader import Reader
from tutor_rag.retrieval import Retrieval
from tutor_rag.generator import Generator
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage

warnings.filterwarnings("ignore", category=DeprecationWarning)

st.set_page_config(
    page_title="RAGenerate: AI Tutor",
    page_icon="🗒️🖋️"
)

# Load Lottie animations
try:
    with open(os.path.join("dsn", "Animation - 1732444487790.json"), "r") as file:
        url = json.load(file)
    with open(os.path.join("dsn", "Animation - 1735054983175.json"), "r") as file:
        theme = json.load(file)
except FileNotFoundError:
    st.error("Lottie animation files not found. Please check the file paths in './dsn/'.")
    url = theme = {}
    st.warning("Using empty Lottie animations as fallback.")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = InMemoryChatMessageHistory()
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
if "retriever" not in st.session_state:
    st.session_state.retriever = None
if "uploaded_file_path" not in st.session_state:
    st.session_state.uploaded_file_path = None

def process_rag(file_path, query, mode):
    """Process RAG pipeline with chat history."""
    try:
        # Read document using Reader class
        reader = Reader(file_path)
        doc = reader.read()

        # Initialize Retrieval if not already done or if file changed
        if st.session_state.vectorstore is None or st.session_state.uploaded_file_path != file_path:
            rtrv = Retrieval(doc)
            st.session_state.vectorstore = rtrv.vectorstore
            st.session_state.retriever = rtrv.retriever
            st.session_state.uploaded_file_path = file_path

        # Retrieve relevant content
        n_query = 7 if mode == "Turbo Mode" else 3
        st.write(f"**Query sent to retriever**: {query}")
        contents = st.session_state.retriever.invoke(query)
        st.write(f"**Retrieved Documents ({len(contents)}):**")
        for doc in contents:
            st.write(f"- {doc.metadata.get('source', 'Unknown')} | Snippet: {doc.page_content[:100]}...")

        # Generate response with history
        gen = Generator()
        chat_history = st.session_state.chat_history.messages
        response = gen.smart_mode(query, contents, chat_history) if mode == "Smart Mode" else gen.turbo_mode(query, contents, chat_history)

        # Update chat history
        st.session_state.chat_history.add_user_message(query)
        st.session_state.chat_history.add_ai_message(response)

        return response, contents
    except Exception as e:
        st.error(f"Error processing query: {e}")
        return "Sorry, an error occurred.", []

# Streamlit App Interface
def main():
    st.markdown('<center><h1> RAGenerate </h1></center>', unsafe_allow_html=True)
    st_lottie(theme, height=200, key="theme")
    st.markdown('<center><h1> The AI Tutor System </h1></center>', unsafe_allow_html=True)

    # Select mode
    mode = st.radio("Select Mode", ["Smart Mode", "Turbo Mode"])

    # File uploader
    uploaded_file = st.file_uploader("Upload a PDF, Word, or Text File", type=["pdf", "docx", "txt"])

    # Display chat history
    st.subheader("Chat History")
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.chat_history.messages:
            if isinstance(msg, HumanMessage):
                st.markdown(f"**You**: {msg.content}")
            else:
                st.markdown(f"**AI Tutor**: {msg.content}")

    # Query input
    query = st.chat_input("Enter your query:")

    # Process file and query
    if uploaded_file and query:
        # Save uploaded file
        file_extension = uploaded_file.name.split(".")[-1].lower()
        file_path = f"uploaded_file.{file_extension}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())

        # Process RAG with spinner
        with st_lottie_spinner(url, loop=True, height=200, width=700):
            response, sources = process_rag(file_path, query, mode)

        # Display response
        st.subheader("Generated Response:")
        st.write(response)

        # Update chat history display
        with chat_container:
            st.markdown(f"**You**: {query}")
            st.markdown(f"**AI Tutor**: {response}")

if __name__ == "__main__":
    main()