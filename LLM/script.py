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
knowledge=[]
def embed(text):
    '''
    Embed function : Embedding for text chunks extracted from the paragraphs we seperated.
    '''
    return(requests.post("http://localhost:11434/api/embed",
                         json={"model": "mxbai-embed-large", "input": text}).json()["embeddings"][0])
for i in range (length_chunks):
    vector = embed(chunks[i])
    knowledge.append({"text":chunks[i] ,"vector":vector})
def retrieve(prompt):
    '''Retrieve Function : Contains 4 steps:
    1/Embed the prompt the user typed
    2/Create Cos_list
    3/Distinguish for each paragraph(a.k.a text) the cosine_sim
    4/sort the cosine_sim
    5/return the best'''
    vector_prompt = embed(prompt)
    cos_list = []
    for i in range(len(knowledge)):
        cos_list.append({"score":cosine_sim(vector_prompt,knowledge[i]["vector"]),"text":knowledge[i]["text"]})
    ranked = sorted(cos_list,key=lambda item : item["score"],reverse=True)
    return ranked[0]["text"]

while 1 :
        prompt = input("Enter your text : ")
        system_msg = {"role": "system", "content": "You are support for Nexalytics. Answer only from these docs: " + retrieve(prompt)}    
        messages.append({"role": "user","content": prompt})
        r = requests.post('https://ollama.com/api/chat', 
                        headers= {"Authorization": "Bearer " + os.environ['OLLAMA_API_KEY']},
                        json= {"model": "gpt-oss:120b", "messages": [system_msg] + messages, "stream": False })
        response_llm=(r.json()["message"]["content"])
        messages.append({"role":"assistant","content": response_llm})
        print(response_llm)     