# Enhanced Q&A Chatbot Applications

## Overview
This repository contains two Streamlit-based chatbot applications:
1. An Ollama LLM-powered chatbot
2. An OpenAI GPT-powered chatbot

These applications provide interactive question-answering interfaces with configurable settings.

## Prerequisites

### Common Requirements
- Python 3.8+
- Streamlit
- LangChain
- python-dotenv

### Ollama Chatbot Additional Requirements
- Ollama installed locally
- Ollama models (mistral, llama2, deepseek-r1, llama3.2)

### OpenAI Chatbot Additional Requirements
- OpenAI API Key

## Installation

1. Clone the repository
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install streamlit langchain python-dotenv
pip install openai  # For OpenAI chatbot
```

## Configuration

### Ollama Chatbot
- Ensure Ollama is installed and models are available
- No API key required

### OpenAI Chatbot
1. Create a `.env` file in the project root
2. Add your OpenAI API key
```
OPENAI_API_KEY=your_openai_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

## Running the Applications

### Ollama Chatbot
```bash
streamlit run ollama_chatbot.py
```

### OpenAI Chatbot
```bash
streamlit run openai_chatbot.py
```

## Features

### Ollama Chatbot
- Model Selection: Choose from Mistral, Llama2, DeepSeek, Llama3.2
- Temperature Control
- Max Tokens Configuration

### OpenAI Chatbot
- Model Selection: GPT-4o, GPT-4 Turbo, GPT-4
- API Key Input
- Temperature Control
- Max Tokens Configuration

## Customization
- Modify the system prompt in `ChatPromptTemplate` to change bot behavior
- Adjust sidebar settings to fine-tune model performance

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
[Specify your license here, e.g., MIT License]

## Acknowledgments
- Streamlit
- LangChain
- Ollama
- OpenAI

## Troubleshooting
- Ensure all dependencies are installed
- Check API keys and environment variables
- Verify Ollama models are correctly installed
