# AIFlux Advanced Chat

AIFlux is an advanced chat interface that allows users to interact with cutting-edge AI models in real time. It offers multiple AI model options, intelligent conversation memory, and a user-friendly interface for smooth and efficient communication.

## Features

- **Multiple AI Models**: Choose from various pre-trained AI models to suit your needs.
- **Real-time Streaming Responses**: Receive instant replies with a typing effect for a more natural conversation.
- **Conversation History**: The AI assistant remembers previous interactions, making for a more continuous and engaging chat experience.
- **Customizable UI**: The app has a clean and responsive design, optimized for different screen sizes.
- **Conversation Management**: Clear conversations with a simple button click and start fresh whenever needed.

## Getting Started

To run the AIFlux Advanced Chat app on your local machine, follow these steps:

### Prerequisites

1. **Python**: Make sure you have Python 3.8 or higher installed.
2. **Virtual Environment (optional but recommended)**: Use `venv` to manage dependencies.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/chandan0813/aiflux-advanced-chat.git
   cd aiflux-advanced-chat
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
4. Set up environment variables: Create a .env file in the project root and add your Groq API key:
   ```bash
   GROQ_API_KEY=your_groq_api_key_here

5. Run the Streamlit app:
   ```bash
   streamlit run app.py
   
6. Open your browser and navigate to http://localhost:8501 to start using the chat interface.

### Usage
   1. Select an AI model from the sidebar to interact with.
   2. Type your message in the input box at the bottom and hit Enter to send.
   3. The AI will respond in real time with a natural typing effect.
   4. You can view your chat history and interact with the AI based on the conversation context.
   5. The Clear Conversation button allows you to start a fresh conversation anytime.


### Code Overview
   app.py
The main application code for running the chat interface using Streamlit.

GroqAPI Class
Handles interactions with the Groq API, including fetching responses from the selected AI model.

Message Class
Manages the chat messages, including adding user and assistant messages, and displaying the chat history.

ModelSelector Class
Allows users to choose the AI model they want to interact with.

custom_css() function
Customizes the look and feel of the chat interface using CSS to enhance user experience.

sidebar() function
Handles the sidebar layout, model selection, and conversation controls like clearing the chat.


