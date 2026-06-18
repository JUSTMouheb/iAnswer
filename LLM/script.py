from dotenv import load_dotenv
import os
import requests
key = load_dotenv()
i=0
prompts = {}
messages=[]
while 1 :
    i+=1
    prompt = input("Enter your text : ")
    messages.append({"role": "user","content": prompt})
    r = requests.post('https://ollama.com/api/chat', 
                        headers= {"Authorization": "Bearer " + os.environ['OLLAMA_API_KEY']},
                        json= {"model": "gpt-oss:120b", "messages": messages, "stream": False })
    response_llm=(r.json()["message"]["content"])
    messages.append({"role":"assistant","content": response_llm})
    print(response_llm)