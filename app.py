import json
import time
import warnings
import streamlit as st
from streamlit_lottie import st_lottie 
from tutor_rag.reader import Reader
from tutor_rag.retrieval import Retrieval
from tutor_rag.generator import Generator
from streamlit_lottie import st_lottie_spinner
warnings.filterwarnings("ignore", category=DeprecationWarning)


st.set_page_config(
    page_title="RAGenerate:AI Tutor",
    page_icon="🗒️🖋️"
)

path = r".\dsn\Animation - 1732444487790.json"
with open(path,"r") as file: 
    url = json.load(file) 
    file.close()
with open(r".\dsn\Animation - 1735054983175.json","r") as file:
    theme = json.load(file)
    file.close()
  

def process_rag(file_path, query, mode):
    # Read PDF content using Reader class
    ext = file_path.split(".")[-1]
    file = Reader(file_path)
    
    if ext == 'docx':
        doc = file.read_word()
    else:
        doc = file.read_pdf()

    n_query = 3
    if mode == 'Turbo Mode':
        n_query = 7
    
    # Retrieve relevant content using Retrieval class
    rtrv = Retrieval(doc)
    contents = rtrv.ask_query(query, n_query)
    print(contents)
    
    # Generate response using Generator class
    gen = Generator()
    if mode == 'Turbo Mode':
        generated = gen.turbo_mode(query, contents)
    else:
        generated = gen.smart_mode(query, contents)
    
    return generated


# Streamlit App Interface
def main():
    # Title of the app
    st.markdown('<center><h1> RAGenerate </h1></center>', unsafe_allow_html=True)
    st_lottie(theme)
    st.markdown('<center><h1> The AI Tutor System </h1></center>', unsafe_allow_html=True)

    # Select the mode
    mode = st.radio("Select Mode", ["Smart Mode", "Turbo Mode"])

    # File uploader widget
    uploaded_file = st.file_uploader("Upload a PDF File", type=["pdf"])

    # Input for the query
    query = st.chat_input("Enter your query:")
    
    # Input for the number of documents to retrieve

    # If a file is uploaded and a query is provided, process the file
    if uploaded_file and query:
        # Save the uploaded PDF to a temporary location
        with open("uploaded_file.pdf", "wb") as f:
            f.write(uploaded_file.read())

        # Process the PDF and generate a response
        with st_lottie_spinner(url,loop=True,height=200,width=700):
            result = process_rag("uploaded_file.pdf", query, mode)
        
        # Display the result
        st.subheader("Generated Response:")
        st.write(result)


# Run the Streamlit app
if __name__ == "__main__":
    main()
