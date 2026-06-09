from dotenv import load_dotenv
import os
import requests
key = load_dotenv()
while 1:
    prompt = input("Enter your text : ")
    r = requests.post('https://ollama.com/api/generate', 
                    headers= {"Authorization": "Bearer " + os.environ['OLLAMA_API_KEY']},
                    json= {"model": "gpt-oss:120b", "prompt": prompt, "stream": False })
    print(r.text)
    
