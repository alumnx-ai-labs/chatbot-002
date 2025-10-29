"""
Streamlit Frontend for Restaurant Chatbot
==========================================
This script creates an interactive web interface for the restaurant chatbot.

Features:
- Chat interface with message history
- User-friendly input field
- Responsive design with custom styling
- Session state management for conversation continuity

Purpose: Teaching Streamlit UI development for AI chatbots
"""

import streamlit as st
from chatbot import RestaurantChatbot
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Restaurant Chatbot",
    page_icon="🍽️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI with black background
st.markdown("""
    <style>
    /* Force black background in all modes */
    .main {
        background-color: #000000 !important;
    }
    
    .stApp {
        background-color: #000000 !important;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1a1a1a !important;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        background-color: #1a1a1a !important;
    }
    
    /* Header styling */
    header[data-testid="stHeader"] {
        background-color: #000000 !important;
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        background-color: #2a2a2a !important;
        color: #ffffff !important;
        border: 1px solid #404040 !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #888888 !important;
    }
    
    /* Chat message containers */
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.8rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    /* User message styling - Blue bubble */
    .user-message {
        background-color: #1e3a5f !important;
        border-left: 5px solid #2196f3;
        color: #ffffff !important;
    }
    
    /* Bot message styling - Green bubble */
    .bot-message {
        background-color: #1a3d1a !important;
        border-left: 5px solid #4caf50;
        color: #ffffff !important;
    }
    
    /* Message header styling */
    .message-header {
        font-weight: bold;
        margin-bottom: 0.5rem;
        color: #ffffff !important;
    }
    
    /* Message content styling */
    .message-content {
        color: #ffffff !important;
        line-height: 1.6;
    }
    
    /* Title styling */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    
    /* Paragraph and text styling */
    p, span, div, label {
        color: #ffffff !important;
    }
    
    /* Info/Success/Error/Warning box styling */
    .stAlert {
        background-color: #2a2a2a !important;
        color: #ffffff !important;
    }
    
    .stAlert > div {
        color: #ffffff !important;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #2196f3 !important;
        color: white !important;
        border: none !important;
        border-radius: 0.5rem;
    }
    
    .stButton > button:hover {
        background-color: #1976d2 !important;
    }
    
    /* Markdown text in sidebar */
    [data-testid="stSidebar"] .element-container {
        color: #ffffff !important;
    }
    
    [data-testid="stSidebar"] p {
        color: #ffffff !important;
    }
    
    [data-testid="stSidebar"] li {
        color: #ffffff !important;
    }
    
    /* Success messages */
    .stSuccess {
        background-color: #1a3d1a !important;
        color: #ffffff !important;
    }
    
    .stSuccess > div {
        color: #ffffff !important;
    }
    
    /* Error messages */
    .stError {
        background-color: #3d1a1a !important;
        color: #ffffff !important;
    }
    
    .stError > div {
        color: #ffffff !important;
    }
    
    /* Warning messages */
    .stWarning {
        background-color: #3d3d1a !important;
        color: #ffffff !important;
    }
    
    .stWarning > div {
        color: #ffffff !important;
    }
    
    /* Info messages */
    .stInfo {
        background-color: #1a2a3d !important;
        color: #ffffff !important;
    }
    
    .stInfo > div {
        color: #ffffff !important;
    }
    
    /* Spinner styling */
    .stSpinner > div {
        border-top-color: #2196f3 !important;
    }
    
    /* Markdown in main area */
    .main .element-container {
        color: #ffffff !important;
    }
    
    /* Override any remaining white backgrounds */
    div[data-testid="stVerticalBlock"] {
        background-color: transparent !important;
    }
    
    div[data-testid="column"] {
        background-color: transparent !important;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #2a2a2a !important;
        color: #ffffff !important;
    }
    
    .streamlit-expanderContent {
        background-color: #1a1a1a !important;
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)


def initialize_session_state():
    """
    Initialize Streamlit session state variables.
    This ensures conversation history persists across reruns.
    """
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    if 'chatbot' not in st.session_state:
        st.session_state.chatbot = None
    
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []


def display_message(role: str, content: str):
    """
    Display a chat message with appropriate styling.
    
    Args:
        role (str): 'user' or 'assistant'
        content (str): Message content
    """
    if role == "user":
        st.markdown(f"""
            <div class="chat-message user-message">
                <div class="message-header">👤 You</div>
                <div class="message-content">{content}</div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="chat-message bot-message">
                <div class="message-header">🤖 Restaurant Assistant</div>
                <div class="message-content">{content}</div>
            </div>
            """, unsafe_allow_html=True)


def main():
    """
    Main application function that handles the UI and chatbot interaction.
    """
    # Initialize session state
    initialize_session_state()
    
    # Check if API key exists in environment
    api_key = os.getenv("GOOGLE_API_KEY")
    
    # Header
    st.title("🍽️ Restaurant Recommendation Chatbot")
    st.markdown("---")
    
    # Sidebar for information and controls
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Display API key status
        if api_key and api_key != "your_google_gemini_api_key_here":
            st.success("✅ API Key loaded from .env file")
            
            # Initialize chatbot button
            if st.session_state.chatbot is None:
                if st.button("Initialize Chatbot", type="primary"):
                    try:
                        st.session_state.chatbot = RestaurantChatbot(api_key)
                        st.success("✅ Chatbot initialized successfully!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Error initializing chatbot: {str(e)}")
            else:
                st.info("✅ Chatbot is ready!")
        else:
            st.error("❌ API Key not found!")
            st.warning("""
            Please add your Google Gemini API key to the .env file:
            
            1. Create a .env file in the project root
            2. Add: GOOGLE_API_KEY=your_api_key_here
            3. Restart the application
            """)
        
        st.markdown("---")
        
        # Information section
        st.header("ℹ️ About")
        st.markdown("""
        This chatbot can help you:
        - 🔍 Find restaurants by cuisine
        - 📋 Get restaurant details
        - 📅 Check reservation availability
        
        **Supported Cuisines:**
        - Indian 🍛
        - Italian 🍕
        - Chinese 🥢
        - Mexican 🌮
        """)
        
        st.markdown("---")
        
        # Clear chat button
        if st.button("🗑️ Clear Chat History"):
            st.session_state.messages = []
            st.session_state.chat_history = []
            st.success("Chat history cleared!")
            st.rerun()
        
        st.markdown("---")
        
        # Example queries
        st.header("💡 Example Queries")
        st.markdown("""
        Try asking:
        - "Show me Indian restaurants"
        - "Tell me about Spice Palace"
        - "Can I book a table for 4 at Pizza Bella on 2024-11-15?"
        """)
    
    # Main chat interface
    if st.session_state.chatbot is None:
        st.info("👈 Please click 'Initialize Chatbot' in the sidebar to start chatting!")
    else:
        # Display chat history
        st.subheader("💬 Chat")
        
        # Container for chat messages
        chat_container = st.container()
        
        with chat_container:
            for message in st.session_state.messages:
                display_message(message["role"], message["content"])
        
        # Chat input at the bottom
        st.markdown("---")
        
        # User input
        user_input = st.text_input(
            "Type your message here...",
            key="user_input",
            placeholder="Ask me about restaurants!",
            label_visibility="collapsed"
        )
        
        # Send button
        col1, col2, col3 = st.columns([6, 1, 1])
        with col2:
            send_button = st.button("Send", type="primary", use_container_width=True)
        
        # Process user input
        if send_button and user_input:
            # Add user message to chat history
            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })
            
            # Get bot response
            with st.spinner("🤔 Thinking..."):
                try:
                    response, updated_history = st.session_state.chatbot.chat(
                        user_input,
                        st.session_state.chat_history
                    )
                    
                    # Update chat history
                    st.session_state.chat_history = updated_history
                    
                    # Add bot response to messages
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response
                    })
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
            
            # Rerun to update the chat display
            st.rerun()
        
        # Display welcome message if no messages yet
        if len(st.session_state.messages) == 0:
            st.info("👋 Hello! I'm your restaurant assistant. How can I help you find the perfect place to eat today?")


# Run the app
if __name__ == "__main__":
    main()