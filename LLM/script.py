from dotenv import load_dotenv
import os
import requests
key = load_dotenv()
i=0
while 1 :
    i+=1
    prompt = input("Enter your text : ")
    prompts = []
    prompts.append(prompt)
    r = requests.post('https://ollama.com/api/generate', 
                        headers= {"Authorization": "Bearer " + os.environ['OLLAMA_API_KEY']},
                        json= {"model": "gpt-oss:120b", "prompt": prompts[len(prompts)-1], "stream": False })
    print(r.text)
    
