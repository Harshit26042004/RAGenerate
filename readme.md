# 📚 RAG Tutor: Document-Grounded Mentoring System

**RAG Tutor** is a Streamlit-based **Retrieval-Augmented Generation (RAG)** application designed to provide personalized tutoring and mentoring based on your uploaded documents. This system processes documents like PDFs and DOCX files, retrieves relevant content, and uses a Large Language Model (LLM) to generate accurate, contextual answers and explanations.

---

## ✨ Features

* **Multi-Document Support:** Easily upload and process `.pdf`, `.docx`, and `.txt` files.
* **Contextual Q&A:** The RAG pipeline grounds all answers **strictly** in the content of your documents, minimizing LLM hallucination.
* **Intuitive UI:** Built with **Streamlit** for a simple, interactive, and fast chat interface.
* **Vector Database:** Uses **ChromaDB** to efficiently store and retrieve document embeddings (vector representations) for rapid similarity search.
* **LangChain Orchestration:** Utilizes the LangChain framework to manage the entire RAG workflow: document loading, chunking, embedding, retrieval, and response generation.

---

## 🛠️ Technology Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Frontend/UI** | Streamlit | Interactive web application interface. |
| **Orchestration** | LangChain | Framework connecting the LLM, documents, and vector store. |
| **Vector DB** | ChromaDB | Stores document embeddings for efficient retrieval. |
| **Document Parsing** | `pypdf`, `python-docx` | Libraries to read and extract text from various file formats. |
| **Backend** | Python 3.x | Core programming language. |

---

## 🚀 Setup and Installation

### Prerequisites

1.  **Python:** Ensure you have **Python 3.8+** installed.
2.  **API Key:** An API key for your chosen Large Language Model (e.g., OpenAI, Google Gemini, etc.).

### Installation Steps

1.  **Clone the Repository:**
    ```bash
    git clone [YOUR-REPO-URL]
    cd rag-tutor-system
    ```
2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    # Activate on Linux/macOS
    source venv/bin/activate
    # Activate on Windows
    .\venv\Scripts\activate
    ```
3.  **Install Dependencies:**
    You'll need the `requirements.txt` file (see the next section) to install all necessary packages.
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set API Key:**
    Set your LLM API key as an environment variable in the ./rag_tutor/generator.py (`GEMINI_API_KEY`).
    ```python
    os.environ["GOOGLE_API_KEY"] = "********YOUR-API-KEY********"
    ```
    *(Note: Streamlit deployments often use `st.secrets` for security.)*

5.  **Run the Application:**
    ```bash
    streamlit run app.py # Replace app.py with your main Streamlit file
    ```

---
