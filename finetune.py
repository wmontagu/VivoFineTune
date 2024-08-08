from openai import OpenAI
import os
client = OpenAI()
directory = 'messages'

for filename in os.listdir(directory):
    client.files.create(file=open(filename, "rb"), 
        purpose="fine-tune"
)