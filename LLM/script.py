from dotenv import load_dotenv
import os
import requests
key = load_dotenv()
r = requests.post('https://ollama.com/api/generate', 
                headers= {"Authorization": "Bearer " + os.environ['OLLAMA_API_KEY']},
                json= {"model": "gpt-oss:120b", "prompt": "Why is the sky blue?", "stream": False })
print(r.text)
