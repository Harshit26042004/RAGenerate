import os
os.environ["GOOGLE_API_KEY"] = "********YOUR-API-KEY********"

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

class Generator:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI tutor. Use the provided context and chat history to answer the question accurately. If you don't know, say so."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "Context: {context}\n\nQuestion: {question}")
        ])
        self.chain = self.prompt | self.llm | StrOutputParser()

    def smart_mode(self, query: str, contents: list, chat_history: list = []) -> str:
        """Generate response in Smart Mode with provided context and history."""
        context = "\n\n".join(doc.page_content for doc in contents)  # Changed to page_content
        return self.chain.invoke({"question": query, "context": context, "chat_history": chat_history})

    def turbo_mode(self, query: str, contents: list, chat_history: list = []) -> str:
        """Generate response in Turbo Mode (same as Smart Mode for now)."""
        return self.smart_mode(query, contents, chat_history)
