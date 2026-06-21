from dotenv import load_dotenv
import os
import requests
f=open("docs/About.txt",'r')
docs=f.read()
key = load_dotenv()
messages=[]
messages.append({"role":"system","content":"You are support for Nexalytics. Answer only from these docs: " + docs})
while 1 :
    prompt = input("Enter your text : ")
    messages.append({"role": "user","content": prompt})
    r = requests.post('https://ollama.com/api/chat', 
                        headers= {"Authorization": "Bearer " + os.environ['OLLAMA_API_KEY']},
                        json= {"model": "gpt-oss:120b", "messages": messages, "stream": False })
    response_llm=(r.json()["message"]["content"])
    messages.append({"role":"assistant","content": response_llm})
    print(response_llm)
