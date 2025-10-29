"""
Restaurant Chatbot using LangChain and Google Gemini
====================================================
This module implements a restaurant recommendation chatbot that can:
- Search restaurants by cuisine type
- Provide detailed restaurant information
- Check reservation availability

Author: Educational Example
Purpose: Teaching AI agent development with LangChain
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from typing import List, Dict, Union
import os


class RestaurantChatbot:
    """
    A chatbot class that handles restaurant-related queries using AI agents.
    
    The chatbot uses LangChain's agent framework with custom tools to:
    - Search for restaurants by cuisine
    - Retrieve detailed restaurant information
    - Check reservation availability
    """
    
    def __init__(self, api_key: str):
        """
        Initialize the chatbot with Google Gemini API.
        
        Args:
            api_key (str): Google Gemini API key
        """
        # Set the API key in environment
        os.environ["GOOGLE_API_KEY"] = api_key
        
        # Initialize the Gemini model
        self.model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp")
        
        # Create tools and agent
        self.tools = self._create_tools()
        self.agent_executor = self._create_agent()
    
    def _create_tools(self) -> List:
        """
        Create the list of tools available to the agent.
        
        Returns:
            List: List of LangChain tools
        """
        @tool
        def search_restaurants_by_cuisine(cuisine_type: str) -> Union[List[Dict], str]:
            """
            Search for restaurants by cuisine type.
            
            Args:
                cuisine_type (str): Type of cuisine (Indian, Italian, Chinese, Mexican)
            
            Returns:
                List[Dict] or str: List of restaurants or error message
            """
            # Restaurant database (in production, this would be a real database)
            restaurants = {
                "indian": [
                    {"name": "Spice Palace", "rating": 4.5, "price": "₹₹"},
                    {"name": "Curry House", "rating": 4.3, "price": "₹₹"},
                    {"name": "Taj Flavors", "rating": 4.7, "price": "₹₹₹"}
                ],
                "italian": [
                    {"name": "Pizza Bella", "rating": 4.4, "price": "₹₹"},
                    {"name": "Pasta Dreams", "rating": 4.6, "price": "₹₹₹"},
                    {"name": "Roma Kitchen", "rating": 4.2, "price": "₹₹"}
                ],
                "chinese": [
                    {"name": "Dragon House", "rating": 4.5, "price": "₹₹"},
                    {"name": "Ming's Kitchen", "rating": 4.3, "price": "₹₹"},
                    {"name": "Golden Wok", "rating": 4.8, "price": "₹₹₹"}
                ],
                "mexican": [
                    {"name": "Taco Fiesta", "rating": 4.4, "price": "₹₹"},
                    {"name": "Salsa Nights", "rating": 4.6, "price": "₹₹₹"},
                    {"name": "Burrito House", "rating": 4.2, "price": "₹₹"}
                ]
            }
            
            # Search for cuisine (case-insensitive)
            cuisine_lower = cuisine_type.lower()
            results = restaurants.get(cuisine_lower, [])
            
            return results if results else f"No restaurants found for {cuisine_type} cuisine"
        
        @tool
        def get_restaurant_details(restaurant_name: str) -> Dict:
            """
            Get detailed information about a specific restaurant.
            
            Args:
                restaurant_name (str): Name of the restaurant
            
            Returns:
                Dict: Restaurant details including address, phone, hours, and specialties
            """
            # Detailed restaurant information database
            details = {
                "Spice Palace": {
                    "cuisine": "Indian",
                    "rating": 4.5,
                    "address": "123 Food Street, City Center",
                    "phone": "9876543210",
                    "hours": "11 AM - 11 PM",
                    "speciality": "Butter Chicken, Biryani"
                },
                "Pizza Bella": {
                    "cuisine": "Italian",
                    "rating": 4.4,
                    "address": "456 Dine Avenue, Downtown",
                    "phone": "9123456789",
                    "hours": "12 PM - 10:30 PM",
                    "speciality": "Margherita Pizza, Tiramisu"
                },
                "Dragon House": {
                    "cuisine": "Chinese",
                    "rating": 4.5,
                    "address": "789 Noodle Lane, Market Area",
                    "phone": "9111222333",
                    "hours": "11:30 AM - 11 PM",
                    "speciality": "Hakka Noodles, Fried Rice"
                },
                "Taco Fiesta": {
                    "cuisine": "Mexican",
                    "rating": 4.4,
                    "address": "321 Spice Row, Hip District",
                    "phone": "9222333444",
                    "hours": "1 PM - 12 AM",
                    "speciality": "Fish Tacos, Guacamole"
                },
                "Curry House": {
                    "cuisine": "Indian",
                    "rating": 4.3,
                    "address": "555 Flavor Street, Old Town",
                    "phone": "9333444555",
                    "hours": "11 AM - 10 PM",
                    "speciality": "Paneer Tikka, Dal Makhani"
                },
                "Taj Flavors": {
                    "cuisine": "Indian",
                    "rating": 4.7,
                    "address": "999 Taste Lane, Premium Zone",
                    "phone": "9444555666",
                    "hours": "12 PM - 11 PM",
                    "speciality": "Biryani, Tandoori Chicken"
                },
                "Pasta Dreams": {
                    "cuisine": "Italian",
                    "rating": 4.6,
                    "address": "777 Pasta Street, Gourmet District",
                    "phone": "9555666777",
                    "hours": "12 PM - 11 PM",
                    "speciality": "Carbonara, Lasagna"
                },
                "Roma Kitchen": {
                    "cuisine": "Italian",
                    "rating": 4.2,
                    "address": "888 Roma Road, Little Italy",
                    "phone": "9666777888",
                    "hours": "11 AM - 10 PM",
                    "speciality": "Wood-fired Pizza, Risotto"
                },
                "Ming's Kitchen": {
                    "cuisine": "Chinese",
                    "rating": 4.3,
                    "address": "444 Dragon Street, Chinatown",
                    "phone": "9777888999",
                    "hours": "11 AM - 10:30 PM",
                    "speciality": "Dim Sum, Sweet and Sour Chicken"
                },
                "Golden Wok": {
                    "cuisine": "Chinese",
                    "rating": 4.8,
                    "address": "333 Fortune Road, East District",
                    "phone": "9888999000",
                    "hours": "12 PM - 11 PM",
                    "speciality": "Peking Duck, Szechuan Noodles"
                },
                "Salsa Nights": {
                    "cuisine": "Mexican",
                    "rating": 4.6,
                    "address": "222 Fiesta Avenue, Entertainment District",
                    "phone": "9999000111",
                    "hours": "2 PM - 12 AM",
                    "speciality": "Enchiladas, Churros"
                },
                "Burrito House": {
                    "cuisine": "Mexican",
                    "rating": 4.2,
                    "address": "111 Spice Lane, Food Court",
                    "phone": "9000111222",
                    "hours": "11 AM - 10 PM",
                    "speciality": "Burritos, Quesadillas"
                }
            }
            
            # Return details or error message
            if restaurant_name in details:
                return details[restaurant_name]
            return {"error": f"Restaurant '{restaurant_name}' not found in system"}
        
        @tool
        def check_reservation_availability(restaurant_name: str, date: str, party_size: int) -> str:
            """
            Check if a restaurant has availability for a reservation.
            
            Args:
                restaurant_name (str): Name of the restaurant
                date (str): Reservation date in YYYY-MM-DD format
                party_size (int): Number of people in the party
            
            Returns:
                str: Availability status message
            """
            # Simulated availability database
            # In production, this would connect to a real reservation system
            available_slots = {
                "Spice Palace": {"2024-11-15": True, "2024-11-16": False, "2024-11-17": True},
                "Pizza Bella": {"2024-11-15": False, "2024-11-16": True, "2024-11-17": True},
                "Dragon House": {"2024-11-15": True, "2024-11-16": True, "2024-11-17": False},
                "Taco Fiesta": {"2024-11-15": True, "2024-11-16": True, "2024-11-17": True},
                "Curry House": {"2024-11-15": True, "2024-11-16": False, "2024-11-17": True},
                "Taj Flavors": {"2024-11-15": False, "2024-11-16": True, "2024-11-17": True}
            }
            
            # Check availability
            if restaurant_name in available_slots:
                is_available = available_slots[restaurant_name].get(date, False)
                if is_available:
                    return f"✓ {restaurant_name} has availability for {party_size} people on {date}"
                else:
                    return f"✗ {restaurant_name} is fully booked for {date}"
            
            return f"Restaurant '{restaurant_name}' not found in system"
        
        # Return list of all tools
        return [
            search_restaurants_by_cuisine,
            get_restaurant_details,
            check_reservation_availability
        ]
    
    def _create_agent(self) -> AgentExecutor:
        """
        Create the LangChain agent with tools and prompt.
        
        Returns:
            AgentExecutor: Configured agent executor
        """
        # Define the system prompt that guides the agent's behavior
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful and friendly restaurant recommendation assistant.
            
            Your capabilities:
            - Help users find restaurants based on their cuisine preferences
            - Provide detailed information about restaurants (address, phone, hours, specialties)
            - Check reservation availability for specific dates
            
            Guidelines:
            - Be conversational and warm in your responses
            - Provide clear, organized information
            - Use emojis occasionally to make the conversation friendly
            - If users are unsure, offer suggestions based on ratings or specialties
            - Always use the available tools to get accurate information
            """),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}")
        ])
        
        # Create the agent with tools and prompt
        agent = create_tool_calling_agent(self.model, self.tools, prompt)
        
        # Create the agent executor
        agent_executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=False,  # Set to True for debugging
            handle_parsing_errors=True
        )
        
        return agent_executor
    
    def chat(self, user_message: str, chat_history: List = None) -> tuple:
        """
        Process a user message and return the chatbot's response.
        
        Args:
            user_message (str): The user's input message
            chat_history (List, optional): Previous conversation history
        
        Returns:
            tuple: (response_text, updated_chat_history)
        """
        if chat_history is None:
            chat_history = []
        
        try:
            # Invoke the agent with user input and history
            result = self.agent_executor.invoke({
                "input": user_message,
                "chat_history": chat_history
            })
            
            # Extract the response
            response = result.get("output", "Sorry, I couldn't process your request.")
            
            return response, chat_history
        
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return error_message, chat_history


# Example usage (for testing purposes)
if __name__ == "__main__":
    # Initialize chatbot (replace with your actual API key)
    API_KEY = "your-api-key-here"
    chatbot = RestaurantChatbot(API_KEY)
    
    # Test conversation
    print("Restaurant Chatbot initialized!")
    print("Ask me about restaurants, or type 'quit' to exit.\n")
    
    history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye! Enjoy your meal! 🍽️")
            break
        
        response, history = chatbot.chat(user_input, history)
        print(f"\nChatbot: {response}\n")