# utils/llm_utils.py
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

load_dotenv()

def initialize_llm():
    """Initialize the Gemini 2.0 Flash model"""
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.7,
        top_p=0.95,
        max_output_tokens=2048,
        safety_settings=[
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
        ]
    )
    return llm

def create_conversation_chain(system_prompt):
    """Create a conversation chain with memory"""
    llm = initialize_llm()
    
    prompt_template = PromptTemplate(
        input_variables=["history", "input"],
        template=f"{system_prompt}\n\nConversation History:\n{{history}}\nHuman: {{input}}\nAI:"
    )
    
    memory = ConversationBufferMemory(return_messages=True)
    
    conversation = ConversationChain(
        llm=llm,
        prompt=prompt_template,
        memory=memory,
        verbose=True
    )
    
    return conversation


def generate_technical_questions(llm, tech_stack):
    """Generate technical questions based on candidate's tech stack"""
    prompt = f"""
    Generate 3-5 technical interview questions for a candidate with the following tech stack:
    {tech_stack}
    
    The questions should:
    1. Be challenging but appropriate for a technical interview
    2. Cover different aspects of the technologies
    3. Include at least one problem-solving question
    4. Be specific to the technologies mentioned
    5. Vary in difficulty level
    6. Include follow-up questions that build upon previous answers when appropriate
    7. Probe deeper into areas where the candidate has shown strength or weakness
    
    Format the response as a numbered list of questions only.
    """
    
    response = llm.invoke(prompt)
    return response.content