from dotenv import load_dotenv
import os
import requests
import numpy as np
f=open("docs/About.txt",'r')
docs=f.read() #Full Text
delimiter = "------------------------------------------------------------------------" #what seperates our paragraphs
chunks = docs.split(delimiter) #chunk = paragraph
chunks = [chunk.strip() for chunk in chunks]
key = load_dotenv()
messages=[]
length_chunks=len(chunks)
#Embedding + Tokenizer
def cosine_sim(A,B):
    return(np.dot(A,B) / (np.linalg.norm(A) * np.linalg.norm(B)))
embeddings=[]
knowledge=[]
for i in range (length_chunks):
    vector= requests.post("http://localhost:11434/api/embed",
                         json={"model": "mxbai-embed-large", "input": chunks[i]}).json()["embeddings"][0]
    knowledge.append({"text":chunks[i] ,"vector":vector})
while 1 :
    prompt = input("Enter your text : ")
    vector_prompt= requests.post("http://localhost:11434/api/embed",
                         json={"model": "mxbai-embed-large", "input": prompt}).json()["embeddings"][0]    
    cos_list=[]
    for i in range(len(knowledge)):
        cos_list.append({"score":cosine_sim(vector_prompt,knowledge[i]["vector"]),"text":knowledge[i]["text"]})
    ranked = sorted(cos_list, key=lambda item: item["score"],reverse=True)
    system_msg = {"role": "system", "content": "You are support for Nexalytics. Answer only from these docs: " + ranked[0]["text"]}    
    messages.append({"role": "user","content": prompt})
    r = requests.post('https://ollama.com/api/chat', 
                        headers= {"Authorization": "Bearer " + os.environ['OLLAMA_API_KEY']},
                        json= {"model": "gpt-oss:120b", "messages": [system_msg] + messages, "stream": False })
    response_llm=(r.json()["message"]["content"])
    messages.append({"role":"assistant","content": response_llm})
    print(response_llm) 