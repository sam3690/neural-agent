# Groq Chatbots with DeepSeek-R1-Distill-Llama-70B

This directory contains two chatbot implementations using the Groq API with the `deepseek-r1-distill-llama-70b` model.

## Prerequisites

1. Make sure you have a Groq API key set in your `.env` file:
   ```
   GROQ_API_KEY="your_groq_api_key_here"
   ```

2. Install dependencies:
   ```bash
   poetry install
   ```

## Chatbot Implementations

### 1. Simple Groq Chatbot (`chatbot.py`)
A straightforward implementation using the Groq Python client directly.

**Features:**
- Direct API calls to Groq
- Conversation history management
- Colored terminal output
- Commands: `quit`, `exit`, `bye`, `clear`

**Run:**
```bash
python langchain\chatbot.py
```

### 2. LangChain Groq Chatbot (`chatbot_langchain.py`)
An implementation that integrates Groq with LangChain for memory management.

**Features:**
- LangChain memory integration
- Structured message handling
- Memory statistics
- Same colored terminal interface
- Commands: `quit`, `exit`, `bye`, `clear`

**Run:**
```bash
python langchain\chatbot_langchain.py
```

## Usage

1. Run either chatbot script
2. Type your messages and press Enter
3. The AI will respond using the DeepSeek-R1-Distill-Llama-70B model
4. Use `clear` to reset conversation history
5. Use `quit`, `exit`, or `bye` to end the conversation

## Model Information

- **Model**: `deepseek-r1-distill-llama-70b`
- **Provider**: Groq
- **Temperature**: 0.7
- **Max Tokens**: 1024

Both implementations maintain conversation context and provide a smooth chatting experience with the powerful DeepSeek model running on Groq's fast inference infrastructure.
