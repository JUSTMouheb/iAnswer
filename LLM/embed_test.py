import os
import requests
response = requests.post("http://localhost:11434/api/embed",
                         json={"model": "mxbai-embed-large", "input": "hello world"})
print(len(response.json()['embeddings'][0]))