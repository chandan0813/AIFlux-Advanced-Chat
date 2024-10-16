import os
import streamlit as st
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import time

# Load environment variables
project_root = Path(__file__).resolve().parent
load_dotenv(project_root / ".env")

class GroqAPI:
    def __init__(self, model_name: str):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model_name = model_name

    def _response(self, message):
        return self.client.chat.completions.create(
            model=self.model_name,
            messages=message,
            temperature=0,
            max_tokens=4096,
            stream=True,
            stop=None,
        )

    def response_stream(self, message):
        for chunk in self._response(message):
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

class Message:
    system_prompt = "You are a professional AI assistant. Please generate helpful and informative responses in English to all user inputs."

    def __init__(self):
        if "messages" not in st.session_state:
            st.session_state.messages = [{"role": "system", "content": self.system_prompt}]
        if "conversation_started" not in st.session_state:
            st.session_state.conversation_started = False

    def add(self, role: str, content: str):
        st.session_state.messages.append({"role": role, "content": content})

    def display_chat_history(self):
        for message in st.session_state.messages:
            if message["role"] == "system":
                continue
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    def display_stream(self, generator):
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""
            for chunk in generator:
                full_response += chunk
                message_placeholder.markdown(full_response + "▌")
                time.sleep(0.01)  # Add a small delay for a more natural typing effect
            message_placeholder.markdown(full_response)
        return full_response

class ModelSelector:
    def __init__(self):
        self.models = ["llama3-70b-8192", "llama3-8b-8192", "mixtral-8x7b-32768", "gemma-7b-it"]

    def select(self):
        return st.selectbox("Select AI Model:", self.models, key="model_selector")

def set_page_config():
    st.set_page_config(
        page_title="AIFlux Advanced Chat",
        page_icon="",
        layout="wide",  # Use wide layout for responsiveness
        initial_sidebar_state="expanded"
    )

def custom_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }
    .stApp {
        background-color: #f0f2f6;
    }
    .main {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stTextInput > div > div > input {
        background-color: #f8f9fa;
        border: 1px solid #ced4da;
        border-radius: 5px;
    }
    .stButton > button {
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #0056b3;
    }
    .stSelectbox {
        background-color: #f8f9fa;
        border-radius: 5px;
    }
    .stChat {
        border-radius: 10px;
        padding: 15px;
        background-color: #ffffff;
        border: 1px solid #e9ecef;
        margin-bottom: 10px;
    }
    .sidebar .sidebar-content {
        background-color: #343a40;
        color: #ffffff;
    }
    
    /* Responsive adjustments */
    @media only screen and (max-width: 768px) {
        .stButton > button, .stTextInput > div > div > input {
            width: 100%;
        }
        .main {
            padding: 15px;
        }
        .stChat {
            padding: 10px;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def sidebar():
    with st.sidebar:
        st.image("aiflux-logo-svg.svg", width=200)
        st.title("AIFlux Advanced Chat")
        st.markdown("---")
        model = ModelSelector()
        selected_model = model.select()
        st.markdown("---")
        st.markdown("Model Information:")
        st.info(f"Selected Model: {selected_model}")
        st.markdown("---")
        st.markdown("Made with ❤️ by Chandramohan pattanaik")
        if st.button("Clear Conversation"):
            st.session_state.messages = [{"role": "system", "content": Message.system_prompt}]
            st.session_state.conversation_started = False
            st.rerun()

    return selected_model

def display_welcome():
    st.title("Welcome to AIFlux Advanced Chat")
    st.subheader("Interact with cutting-edge AI models")
    st.markdown("""
     **Features:**
    - Multiple AI models to choose from
    - Real-time streaming responses
    - Intelligent conversation memory
    - User-friendly interface

    Start by selecting a model in the sidebar and typing your message below!
    """)

def main():
    # Initialize session state variables
    if "conversation_started" not in st.session_state:
        st.session_state.conversation_started = False
    
    set_page_config()
    custom_css()
    selected_model = sidebar()
    
    if not st.session_state.conversation_started:
        display_welcome()

    message = Message()
    message.display_chat_history()

    user_input = st.chat_input("Type your message here...")
    if user_input:
        st.session_state.conversation_started = True
        llm = GroqAPI(selected_model)
        message.add("user", user_input)
        message.display_chat_history()

        with st.spinner("AI is thinking..."):
            response = message.display_stream(llm.response_stream(st.session_state.messages))
        message.add("assistant", response)
    
    # Display some usage tips and information
    with st.expander("Usage Tips & Information"):
        st.markdown("""
        - You can change the AI model at any time using the selector in the sidebar.
        - The conversation history is preserved between model changes.
        - Use the 'Clear Conversation' button in the sidebar to start a new chat.
        - The AI assistant can help with a wide range of tasks, including answering questions, providing explanations, and offering suggestions.
        """)

if __name__ == "__main__":
    main()
