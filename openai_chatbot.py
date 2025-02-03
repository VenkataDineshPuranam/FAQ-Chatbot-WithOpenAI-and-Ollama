from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "FAQ Chatbot Project With Ollama Models"



prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please answer the questions"),
        ("user", "Question:{question}"),
    ]
)


def generate_response(question, llm, temperature, max_tokens):
    llm = OllamaLLM(model=llm)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({"question": question})
    return answer


#Title of the APP.

st.title("Enhanced Q&A Chatbot With OllamaLLM Models")


##Sidebar for settings

st.sidebar.title("Settings")

##Drop down to select variants of the model

llm = st.sidebar.selectbox("Select a LLM:", ["mistral:latest", "llama2:latest", "deepseek-r1:8b", "llama3.2:latest" ])

temperature = st.sidebar.slider("Temperature:", min_value=0.0, max_value=1.0, value=0.5, step=0.1)
max_tokens = st.sidebar.slider("Max Tokens:", min_value=100, max_value=1000, value=500, step=50)

#Main interface for the user input.

st.write("Go ahead and enter your questions")
user_input = st.text_input("You:", "")

if user_input:
    response = generate_response(user_input, llm, temperature, max_tokens)
    st.write("Chatbot:", response)
else:
    st.write("Please enter a question to get started.")
