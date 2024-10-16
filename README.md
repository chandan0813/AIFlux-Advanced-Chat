AIFlux Advanced Chat
AIFlux Advanced Chat is an interactive web application built using Streamlit, powered by cutting-edge AI models for real-time conversation. Users can interact with different models to get responses for a wide range of queries and tasks.

Features
Multiple AI Models: Choose from a variety of AI models to suit your needs.
Real-time Streaming Responses: Get responses streamed in real-time for a natural chat experience.
Conversation Memory: Your conversation history is preserved even when switching models.
Responsive Design: Optimized for both desktop and mobile devices for seamless interaction.
Model Information: Provides detailed information about the selected AI model.
Clear Conversation: Reset the conversation and start fresh at any time.
Tech Stack
Frontend: Streamlit
Backend: Groq API for natural language processing (NLP)
Environment: Python, Pip, dotenv for environment variables
Installation
Prerequisites
Before running the app, ensure you have the following installed:

Python 3.7+
Pip (Python package manager)
Steps to Install
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/aiflux-advanced-chat.git
Navigate to the project directory:

bash
Copy code
cd aiflux-advanced-chat
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file in the project root and add your Groq API key:

makefile
Copy code
GROQ_API_KEY=your_api_key_here
Run the Streamlit app:

bash
Copy code
streamlit run main.py
Open the application in your browser at http://localhost:8501/.

Project Structure
bash
Copy code
/aiflux-advanced-chat
├── main.py             # Main Streamlit app script
├── .env                # Environment variables for API keys
├── requirements.txt     # List of dependencies
├── aiflux-logo-svg.svg  # Logo for the sidebar
└── README.md           # Project documentation
Usage
Select an AI Model: Choose the AI model from the dropdown in the sidebar.
Start Chatting: Type your message in the chat input at the bottom of the page.
Clear Conversation: Click on the "Clear Conversation" button in the sidebar to reset the chat history.
Responsive Design: The app is responsive and works across desktop and mobile devices.
Customization
You can add or modify the AI models in the ModelSelector class within main.py.
Modify the style and design by editing the custom CSS in the custom_css function.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/your-feature).
Open a pull request.
License
This project is open-source and available under the MIT License.

Acknowledgments
Streamlit for making it easy to build beautiful and interactive web apps.
Groq API for providing powerful natural language processing models.
