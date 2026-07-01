# iAnswer
An AI Customer Support Agent Platform  built from scratch (No LangChain): for companies to upload their docs , and the AI agent answers their question
---
## Why iAnswer ?
Nowadays , LLMs are prowerful , but they have certain limitations for example the LLM response could be out of date (trained on old data) for a specific prompt or it has no  source available , it can hallicunate - so it confidently states things that aren't true.
-> iAnswer addresses this by grounding answers in retried and up-to-date sources.
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