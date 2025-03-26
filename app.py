# app.py
import streamlit as st
from utils.llm_utils import create_conversation_chain, initialize_llm, generate_technical_questions
from utils.prompts import SYSTEM_PROMPT, GREETING_MESSAGE
from utils.data_handler import validate_email
import re

# Page configuration
st.set_page_config(
    page_title="Technical Interview Assistant",
    page_icon="💼",
    layout="centered"
)

# Initialize session state
if "conversation" not in st.session_state:
    st.session_state.conversation = create_conversation_chain(SYSTEM_PROMPT)
    
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
if "initialized" not in st.session_state:
    st.session_state.initialized = False

# Title and description
st.title("Technical Interview Assistant")
st.markdown("I'll ask you some questions to understand your technical background and skills.")

# Function to check for exit keywords
def check_exit_keywords(user_input):
    exit_keywords = ["goodbye", "exit", "quit", "end", "bye"]
    return any(keyword in user_input.lower() for keyword in exit_keywords)

# Initialize chat with greeting
if not st.session_state.initialized:
    st.session_state.chat_history.append({"role": "assistant", "content": GREETING_MESSAGE})
    st.session_state.initialized = True

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("Type your response here...")

if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # Display user message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Check for exit keywords
    if check_exit_keywords(user_input):
        response = "Thank you for completing this technical interview. Your responses have been recorded. If selected, our team will contact you for the next steps in the hiring process. Have a great day!"
    else:
        # Get response from LLM
        response = st.session_state.conversation.predict(input=user_input)
    
    # Add assistant response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": response})
    
    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response)
    
    # Auto-scroll to the bottom
    st.experimental_rerun()


# Add to session state initialization
if "interview_stage" not in st.session_state:
    st.session_state.interview_stage = "greeting"
    
if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {
        "name": "",
        "email": "",
        "phone": "",
        "experience": "",
        "position": "",
        "location": "",
        "tech_stack": []
    }

# Function to determine the current interview stage
def update_interview_stage(user_input, assistant_response):
    current_stage = st.session_state.interview_stage
    
    # Extract and update candidate data based on the conversation
    if current_stage == "greeting" and "name" in assistant_response.lower():
        st.session_state.candidate_data["name"] = user_input
        st.session_state.interview_stage = "email"
    elif current_stage == "email":
        if validate_email(user_input):
            st.session_state.candidate_data["email"] = user_input
            st.session_state.interview_stage = "phone"
    # Continue with other stages...
    
    # When tech stack is collected, generate technical questions
    if current_stage == "tech_stack" and user_input:
        tech_stack = user_input
        st.session_state.candidate_data["tech_stack"] = tech_stack.split(", ")
        questions = generate_technical_questions(initialize_llm(), tech_stack)
        st.session_state.interview_stage = "technical_questions"
        
        # Add the questions to the conversation context
        return f"Based on your tech stack, I'd like to ask you some technical questions:\n\n{questions}\n\nPlease answer the first question."
    
    return None