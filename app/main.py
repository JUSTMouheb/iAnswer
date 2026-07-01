from rag import retrieve
from LLM import chat
messages=[]
while True :
    prompt = input("Enter your text : ")
    if prompt == "":
        print("Sorry , you have to write something in order to proceed")
    else:
        system_msg = {"role": "system", 
                    "content": "You are support for Nexalytics. Answer only from these docs: " + retrieve(prompt)}    
        messages.append({"role": "user",
                        "content": prompt})
        response = chat([system_msg] + messages)
        messages.append({"role":"assistant","content":response})
        print(response)