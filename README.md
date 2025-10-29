# Restaurant Chatbot using AI Agents 🍽️

An educational project demonstrating how to build an intelligent restaurant recommendation chatbot using LangChain, Google Gemini, and Streamlit.

## 📚 Learning Objectives

This project teaches students:
- How to build AI agents using LangChain
- Creating custom tools for specific tasks
- Implementing a conversational interface with Streamlit
- Managing chat history and session state
- Integrating Large Language Models (LLMs) with structured data

## 🎯 Features

The chatbot can:
- **Search Restaurants**: Find restaurants by cuisine type (Indian, Italian, Chinese, Mexican)
- **Get Details**: Retrieve complete information about specific restaurants
- **Check Availability**: Verify reservation availability for specific dates

## 📁 Project Structure

```
restaurant-chatbot/
│
├── chatbot.py           # Core chatbot logic with LangChain agents
├── app.py              # Streamlit web interface
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
└── README.md          # Project documentation
```

## 🚀 Complete Setup Instructions

### Prerequisites
- Python 3.8 or higher installed on your system
- Git installed on your system
- A Google account (for Gemini API access)

---

## 📥 Step 1: Clone the Repository

Open your terminal/command prompt and run:

```bash
git clone https://github.com/alumnx-ai-labs/chatbot-002.git
cd chatbot-002
```

---

## 🔑 Step 2: Get Your Google Gemini API Key

### 2.1: Visit Google AI Studio

Go to [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)

### 2.2: Sign In

Sign in with your Google account

### 2.3: Create a Project (if needed)

- If you don't have a project yet, you'll see a button that says **"Create API key in new project"**
- Click on it to create a new project
- If you already have a project, click **"Create API key"** and select your project

### 2.4: Generate API Key

- Click **"Create API key"**
- Your API key will be displayed - it looks something like: `AIza...`
- **IMPORTANT**: Copy this key immediately and store it securely
- You won't be able to see the full key again!

### 2.5: Save Your API Key

Keep this key safe - you'll need it in the next step.

---

## 🔧 Step 3: Set Up Environment Variables

### 3.1: Create .env file

In the project directory, create a new file named `.env` (note the dot at the beginning):

**On Mac/Linux:**
```bash
cp .env.example .env
```

**On Windows (Command Prompt):**
```cmd
copy .env.example .env
```

**On Windows (PowerShell):**
```powershell
Copy-Item .env.example .env
```

### 3.2: Add Your API Key

Open the `.env` file in a text editor and replace `your-api-key-here` with your actual Gemini API key:

```
GOOGLE_API_KEY=AIzaSyBBLOSLFjHL7NJlpK53M_gAgfk059Gr51M
```

**⚠️ SECURITY WARNING**: Never commit the `.env` file to Git! It's already in `.gitignore`.

---

## 🐍 Step 4: Set Up Virtual Environment

A virtual environment keeps your project dependencies isolated from other Python projects.

### For Mac/Linux:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# You should see (venv) at the start of your terminal prompt
```

### For Windows (Command Prompt):

```cmd
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat

# You should see (venv) at the start of your prompt
```

### For Windows (PowerShell):

```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\Activate.ps1

# If you get an execution policy error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Then try activating again
```

**Note**: You'll need to activate the virtual environment every time you open a new terminal session to work on this project.

---

## 📦 Step 5: Install Dependencies

With your virtual environment activated, install the required packages:

```bash
pip install -r requirements.txt
```

This will install:
- Streamlit (web interface)
- LangChain (AI agent framework)
- Google Generative AI (Gemini API)
- Other necessary dependencies

**Wait for installation to complete** - this may take a few minutes.

---

## ▶️ Step 6: Run the Application

With everything set up, start the Streamlit app:

```bash
streamlit run app.py
```

### What happens next:

1. The terminal will show some output
2. Your default web browser will automatically open
3. The app will be running at `http://localhost:8501`
4. If the browser doesn't open automatically, manually visit that URL

---

## 🎮 Step 7: Use the Chatbot

### 7.1: Configure the Chatbot

1. In the sidebar (left side), enter your Google Gemini API key
2. Click the **"Initialize Chatbot"** button
3. Wait for the success message: "✅ Chatbot initialized successfully!"

### 7.2: Start Chatting

Type a message in the input box at the bottom, such as:
- "Show me Indian restaurants"
- "Tell me about Spice Palace"
- "Can I book a table for 4 at Pizza Bella on 2024-11-15?"

---

## 🛑 Stopping the Application

To stop the Streamlit server:
- Press `Ctrl + C` in the terminal
- To deactivate the virtual environment, type: `deactivate`

## 💡 How It Works

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                          User Interface                          │
│                         (Streamlit App)                          │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                    RestaurantChatbot Class                       │
│                        (chatbot.py)                              │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              LangChain Agent Executor                     │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │            Google Gemini LLM                        │  │  │
│  │  │         (Decision Making Brain)                     │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  │                           ↓                               │  │
│  │  ┌────────────────────────────────────────────────────┐  │  │
│  │  │              Tool Selection                         │  │  │
│  │  │   (Agent decides which tool to call)                │  │  │
│  │  └────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────┘  │
│                             │                                    │
│         ┌───────────────────┼───────────────────┐               │
│         ↓                   ↓                   ↓               │
│  ┌─────────────┐   ┌──────────────┐   ┌─────────────────┐     │
│  │   Tool 1:   │   │   Tool 2:    │   │    Tool 3:      │     │
│  │   Search    │   │   Get        │   │    Check        │     │
│  │ Restaurants │   │ Restaurant   │   │ Reservation     │     │
│  │ by Cuisine  │   │   Details    │   │ Availability    │     │
│  └─────────────┘   └──────────────┘   └─────────────────┘     │
│         │                   │                   │               │
│         └───────────────────┼───────────────────┘               │
│                             ↓                                    │
│                    Restaurant Database                           │
│                  (Simulated with Python dicts)                   │
└─────────────────────────────────────────────────────────────────┘
```

### Detailed Component Breakdown

#### 🎨 **1. Frontend Layer - Streamlit (app.py)**

**Responsibilities:**
- Render the user interface
- Handle user input and display messages
- Manage session state (chat history)
- Provide API key configuration interface

**Key Features:**
- **Session State Management**: Uses `st.session_state` to maintain conversation history across page reloads
- **Message Display**: Custom CSS styling for user and bot messages
- **Interactive Input**: Real-time chat input with send button
- **Sidebar Configuration**: Safe API key input and chatbot initialization

**Code Flow:**
1. User enters message
2. Message added to session state
3. Message sent to chatbot backend
4. Response received and displayed
5. UI updates with new message

---

#### 🤖 **2. Core Logic Layer - RestaurantChatbot (chatbot.py)**

**Responsibilities:**
- Initialize and manage the AI agent
- Process user queries
- Coordinate between LLM and tools
- Return formatted responses

**Key Components:**

##### **A. The LangChain Agent**
- **Purpose**: Acts as the "brain" that decides what to do
- **Decision Process**:
  1. Receives user input
  2. Analyzes intent using Gemini LLM
  3. Determines which tool(s) to call
  4. Executes tool(s) in sequence if needed
  5. Formulates natural language response

##### **B. The Google Gemini LLM**
- **Model**: `gemini-2.0-flash-exp`
- **Role**: Natural language understanding and generation
- **Capabilities**:
  - Understands user intent
  - Decides tool usage
  - Generates conversational responses
  - Maintains context from chat history

##### **C. System Prompt**
- Defines the agent's personality and capabilities
- Provides guidelines for responses
- Instructs the agent on tool usage
- Sets conversation tone (friendly, helpful)

**Example Decision Flow:**
```
User: "I want Indian food"
  ↓
Gemini LLM analyzes: "User wants restaurant recommendations"
  ↓
Agent decides: "Use search_restaurants_by_cuisine tool"
  ↓
Tool returns: [List of Indian restaurants]
  ↓
Gemini formats response: "I found 3 great Indian restaurants..."
```

---

#### 🛠️ **3. Tool Layer - Custom Functions**

Each tool is a Python function decorated with `@tool` that the agent can call.

##### **Tool 1: search_restaurants_by_cuisine**
```python
@tool
def search_restaurants_by_cuisine(cuisine_type: str) -> list:
```
- **Purpose**: Find restaurants by cuisine type
- **Input**: Cuisine name (e.g., "indian", "italian")
- **Output**: List of restaurant dictionaries with name, rating, price
- **Data Source**: Hardcoded dictionary (simulates database)

##### **Tool 2: get_restaurant_details**
```python
@tool
def get_restaurant_details(restaurant_name: str) -> dict:
```
- **Purpose**: Get comprehensive information about a specific restaurant
- **Input**: Restaurant name
- **Output**: Dictionary with address, phone, hours, specialties
- **Use Case**: When user asks "Tell me more about X"

##### **Tool 3: check_reservation_availability**
```python
@tool
def check_reservation_availability(restaurant_name: str, date: str, party_size: int) -> str:
```
- **Purpose**: Check if reservation is possible
- **Input**: Restaurant name, date (YYYY-MM-DD), number of people
- **Output**: Availability status message
- **Logic**: Checks against simulated availability calendar

**Why Use Tools?**
- **Structured Data Access**: Tools provide reliable, formatted data
- **Separation of Concerns**: LLM handles language, tools handle data
- **Extensibility**: Easy to add new capabilities
- **Accuracy**: Prevents LLM from hallucinating restaurant info

---

#### 💾 **4. Data Layer - Restaurant Database**

Currently implemented as Python dictionaries:

```python
restaurants = {
    "indian": [
        {"name": "Spice Palace", "rating": 4.5, "price": "₹₹"},
        ...
    ],
    ...
}
```

**In Production:**
- Would be replaced with actual database (PostgreSQL, MongoDB, etc.)
- Could integrate with real APIs (Yelp, Google Places, Zomato)
- Would include real-time availability systems

---

### 🔄 Complete Request Flow Example

Let's trace a complete user interaction:

**User Input:** "I want to eat Italian food tonight"

**Step 1: Frontend (app.py)**
```
User types message → Streamlit captures input → Adds to session state
```

**Step 2: Chatbot Initialization**
```
app.py calls: chatbot.chat("I want to eat Italian food tonight", history)
```

**Step 3: Agent Processing**
```
RestaurantChatbot.chat() → agent_executor.invoke()
```

**Step 4: LLM Analysis**
```
Gemini LLM receives:
- User message: "I want to eat Italian food tonight"
- Available tools: [search_restaurants_by_cuisine, get_restaurant_details, check_reservation_availability]
- System prompt: "You are a helpful restaurant assistant..."

LLM thinks: "User wants Italian restaurants. I should use search_restaurants_by_cuisine tool."
```

**Step 5: Tool Execution**
```
Agent calls: search_restaurants_by_cuisine("italian")
↓
Tool searches database
↓
Returns: [
    {"name": "Pizza Bella", "rating": 4.4, "price": "₹₹"},
    {"name": "Pasta Dreams", "rating": 4.6, "price": "₹₹₹"},
    {"name": "Roma Kitchen", "rating": 4.2, "price": "₹₹"}
]
```

**Step 6: Response Generation**
```
Gemini LLM formats response:
"I found 3 wonderful Italian restaurants for you! 🍝

1. **Pasta Dreams** - Rating: 4.6 ⭐ (₹₹₹)
2. **Pizza Bella** - Rating: 4.4 ⭐ (₹₹)
3. **Roma Kitchen** - Rating: 4.2 ⭐ (₹₹)

Would you like to know more about any of these?"
```

**Step 7: Return to Frontend**
```
Response flows back: chatbot.chat() → app.py → Streamlit display
```

**Step 8: UI Update**
```
Streamlit adds bot message to session state → Renders on screen → User sees response
```

---

### 🧠 Key Architectural Decisions

#### **1. Why LangChain?**
- **Agent Framework**: Built-in support for creating AI agents
- **Tool Integration**: Easy to add custom functions
- **Prompt Templates**: Structured way to guide LLM behavior
- **Chat History**: Built-in memory management

#### **2. Why Google Gemini?**
- **Cost-Effective**: Competitive pricing for educational use
- **Fast**: Flash model provides quick responses
- **Capable**: Handles tool calling and reasoning well
- **Accessible**: Easy to get API key for learning

#### **3. Why Streamlit?**
- **Rapid Development**: Build UI with pure Python
- **No Frontend Skills Needed**: No HTML/CSS/JavaScript required
- **Session State**: Built-in state management for chat apps
- **Interactive**: Real-time updates and user interaction

#### **4. Why Separate chatbot.py and app.py?**
- **Separation of Concerns**: Business logic separate from presentation
- **Testability**: Can test chatbot logic independently
- **Reusability**: Chatbot class can be used in other interfaces (CLI, API, etc.)
- **Maintainability**: Easier to update one component without affecting the other

---

### 🔧 How the Agent Makes Decisions

The agent uses a **ReAct (Reasoning + Acting) pattern**:

1. **Reason**: Analyze the user's request
2. **Act**: Decide which tool to use (if any)
3. **Observe**: See the tool's output
4. **Reason**: Determine if more tools are needed
5. **Respond**: Formulate final answer

**Example Multi-Step Reasoning:**
```
User: "What's the best rated Italian restaurant and can I book it for tomorrow?"

Agent Reasoning:
1. "I need to find Italian restaurants" → Use search_restaurants_by_cuisine
2. "Now I have a list, Pasta Dreams has highest rating (4.6)"
3. "User wants to book for tomorrow" → Use check_reservation_availability
4. "I have all info needed" → Formulate response

Final Response: "The best rated Italian restaurant is Pasta Dreams (4.6⭐)..."
```

This architecture makes the chatbot:
- **Intelligent**: Can handle complex, multi-step queries
- **Accurate**: Uses structured data, not hallucinations
- **Extensible**: Easy to add new capabilities
- **Maintainable**: Clean separation of concerns
- **Educational**: Clear structure for learning

---

### Key Components

#### 1. **Tools** (`chatbot.py`)
Custom functions that the AI agent can call:

- `search_restaurants_by_cuisine()`: Searches database by cuisine type
- `get_restaurant_details()`: Fetches detailed restaurant information
- `check_reservation_availability()`: Checks if reservations are available

#### 2. **Agent** (`chatbot.py`)
The LangChain agent that:
- Understands user intent
- Decides which tools to use
- Formulates natural language responses

#### 3. **Frontend** (`app.py`)
Streamlit interface that:
- Displays chat messages
- Manages conversation history
- Provides user input handling

## 🎓 Teaching Points

### For Students:

1. **Understanding AI Agents**
   - Agents can use tools to accomplish tasks
   - They decide autonomously which tool to call based on user input
   - The LLM acts as the "brain" making these decisions

2. **Tool Design**
   - Each tool has a specific, well-defined purpose
   - Tools use type hints for clarity
   - Docstrings help the AI understand when to use each tool

3. **Conversation Management**
   - Chat history maintains context across messages
   - Session state in Streamlit preserves data between interactions
   - The agent uses history to provide coherent responses

4. **Prompt Engineering**
   - The system prompt guides the agent's behavior
   - Clear instructions result in better responses
   - Personality can be defined through prompts

## 🔧 Customization Ideas

Students can extend this project by:

1. **Adding More Tools**
   - Menu browsing
   - Price comparison
   - Review summaries
   - Distance calculation

2. **Enhancing Data**
   - Connect to a real database
   - Add more restaurants and cuisines
   - Include images and reviews

3. **Improving UI**
   - Add restaurant images
   - Show ratings visually (stars)
   - Display maps with restaurant locations
   - Add filters (price range, rating, distance)

4. **Advanced Features**
   - Multi-language support
   - Voice input/output
   - Recommendation based on preferences
   - Integration with real reservation systems

## 📝 Example Conversations

**Finding Restaurants:**
```
User: I want to eat Indian food
Bot: I found 3 great Indian restaurants for you! [lists restaurants]
```

**Getting Details:**
```
User: Tell me more about Spice Palace
Bot: Spice Palace is an Indian restaurant... [provides complete details]
```

**Checking Availability:**
```
User: Can I book a table for 4 at Spice Palace on 2024-11-15?
Bot: ✓ Spice Palace has availability for 4 people on 2024-11-15
```

## 🛠️ Technical Stack

- **LangChain**: Agent framework and tool integration
- **Google Gemini**: Large Language Model (LLM)
- **Streamlit**: Web application framework
- **Python**: Core programming language

## 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini API](https://ai.google.dev/docs)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## ⚠️ Important Notes

- The restaurant data is hardcoded for demonstration purposes
- The API key should be kept secure and not committed to version control
- In production, use environment variables for sensitive data
- The availability checker uses simulated data

## 🤝 Contributing

Students are encouraged to:
- Add new features
- Improve the UI
- Expand the restaurant database
- Add error handling
- Write tests

## 📄 License

This is an educational project. Feel free to use and modify for learning purposes.

## 🆘 Troubleshooting

**Issue**: "Module not found" error
**Solution**: Make sure all dependencies are installed with `pip install -r requirements.txt`

**Issue**: API key error
**Solution**: Verify your Google Gemini API key is valid and has the necessary permissions

**Issue**: Chatbot not responding
**Solution**: Check the console for error messages and verify internet connectivity

---

**Happy Learning! 🎓**