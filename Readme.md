# TalentScout

## Project Overview
The **Technical Interview Assistant** is an AI-powered chatbot designed to streamline the preliminary technical interview process. Built with **LangChain** and **Google's Gemini 2.0 Flash model**, this application conducts structured conversations with candidates to gather their information and assess their technical skills.

## Key Capabilities
- Collects candidate details (name, email, experience, etc.).
- Identifies the candidate's tech stack.
- Generates tailored technical questions based on declared skills.
- Conducts a natural, conversational technical assessment.
- Maintains context for meaningful follow-up questions.

## Installation Instructions

### Prerequisites
- Python 3.9 or higher
- Google API key with access to Gemini models

### Setup Steps

#### 1. Clone the repository
```bash
git clone https://github.com/yourusername/technical-interview-assistant.git
cd TALENTSCOUT
```

#### 2. Create a virtual environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

#### 3. Install dependencies
```bash
pip install -r requirements.txt
```

#### 4. Set up environment variables
Create a `.env` file in the project root with the following content:
```text
GOOGLE_API_KEY=your_google_api_key_here
```

#### 5. Run the application
```bash
streamlit run app.py
```

#### 6. Access the application
Open your web browser and navigate to **[http://localhost:8501](http://localhost:8501)**

## Usage Guide

### Start the Interview
- The chatbot will greet you and explain its purpose.
- Answer each question to proceed through the interview.

### Provide Personal Information
- The chatbot will ask for your name, email, phone number, etc.
- All information is handled securely and can be anonymized.

### Declare Your Tech Stack
- List the technologies, languages, frameworks, and tools you're proficient in.
- Be specific to receive more relevant technical questions.

### Answer Technical Questions
- The chatbot will generate **3-5** questions based on your tech stack.
- Questions range in difficulty and cover different aspects of each technology.
- The chatbot may ask follow-up questions based on your responses.

### End the Interview
- Type `goodbye`, `exit`, `quit`, or `end` to conclude the interview.
- The chatbot will thank you and explain the next steps.

## Technical Details

### Libraries & Tools
- **LangChain**: Framework for developing applications powered by language models.
- **Google Generative AI**: API for accessing Google's Gemini 2.0 Flash model.
- **Streamlit**: Framework for building the web interface.
- **Python-dotenv**: For loading environment variables.
- **Regular Expressions**: For validating user inputs (email, phone).

### Architecture
The application follows a modular architecture:
- **UI Layer (Streamlit)**
  - Handles user interface and interaction.
  - Manages session state and conversation flow.
- **LLM Integration Layer (LangChain)**
  - Configures and initializes the Gemini model.
  - Creates conversation chains with memory.
  - Processes prompts and responses.
- **Business Logic Layer**
  - Manages interview stages.
  - Validates user inputs.
  - Generates technical questions based on the tech stack.

### Model Details
- **Model**: Google Gemini 2.0 Flash
- **Temperature**: 0.7 (balanced between creativity and consistency)
- **Top-p**: 0.95 (diverse yet focused responses)
- **Max Output Tokens**: 2048 (sufficient for detailed responses)
- **Safety Settings**: Medium threshold for harmful content categories

## Prompt Design

### System Prompt
The system prompt defines the chatbot's role, responsibilities, and constraints. It includes:
- Clear definition of the interview process stages.
- Guidelines for professional and respectful interaction.
- Instructions for handling sensitive information.
- Boundaries to prevent deviation from the interview purpose.

### Technical Question Generation
- Creates questions specifically tailored to the candidate's tech stack.
- Ensures a range of difficulty levels.
- Includes problem-solving scenarios.
- Generates follow-up questions based on previous responses.
- Maintains context from the conversation history.

### Conversation Flow Management
- Guides the candidate through a logical interview process.
- Collects information in a natural, conversational manner.
- Validates inputs without breaking the conversation flow.
- Gracefully handles unexpected responses.

## Challenges & Solutions

### Challenge 1: Maintaining Conversation Context
- **Problem**: The chatbot needed to remember previous responses to ask relevant follow-up questions.
- **Solution**: Implemented **LangChain's ConversationBufferMemory** to maintain conversation history and provide context for the model's responses.

### Challenge 2: Generating Relevant Technical Questions
- **Problem**: Technical questions needed to be specific to the candidate's declared tech stack.
- **Solution**: Created a specialized prompt that extracts the tech stack from the conversation and generates tailored questions with varying difficulty levels.

### Challenge 3: Handling Unexpected Inputs
- **Problem**: Candidates might provide unexpected or irrelevant responses.
- **Solution**: Enhanced the system prompt with fallback mechanisms and added input validation to guide the conversation back on track while maintaining a natural flow.

### Challenge 4: Balancing Structure and Naturalness
- **Problem**: The interview needed to follow a structured process while feeling conversational.
- **Solution**: Designed prompts that guide the model to ask questions in a friendly, conversational tone while still following the required interview stages.

## Conclusion
This project demonstrates the effective use of **LangChain** and **Google's Gemini model** to create an intelligent **technical interview assistant** that can adapt to different candidates and technology stacks while maintaining a professional and engaging conversation.

---
**Contributions are welcome!** If you'd like to improve or expand this project, feel free to submit a pull request or open an issue.

**License:** MIT License
