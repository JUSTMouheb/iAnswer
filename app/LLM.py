from dotenv import load_dotenv
import os
import requests
load_dotenv()
def chat(messages):
        r = requests.post('https://ollama.com/api/chat', 
                        headers= {"Authorization": "Bearer " + os.environ['OLLAMA_API_KEY']},
                        json= {"model": "gpt-oss:120b", "messages": messages, "stream": False })
        return r.json()["message"]["content"]