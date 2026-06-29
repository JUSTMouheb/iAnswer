# iAnswer
An AI Customer Support Agent Platform  built from scratch (No LangChain): for companies to upload their docs , and the AI agent answers their question
---
## Current stage
CLI agent that chats with an LLM , remembers the conversation and answers from a local docs file. 
## Setup & Run
pip install -r requirements.txt
# create a .env with your OLLAMA_API_KEY
ollama pull mxbai-embed-large
python LLM/script.py
## Tools Used
- Ollama Cloud API KEY
- Ollama (mxbai-embed-large) : Embed Model
- Python-dotenv to read .env variables