import os
import pandas as pd
import random
import math
import json
#downlaods messages wihtout emojis (emojis breaks things)

def CreateFilterDiscord(directory, messagesList, file_path):
    for d in os.listdir(directory):
        subdir = os.path.join(directory, d)
        for filename in os.listdir(subdir):
            path = os.path.join(subdir, filename)
            if "channel" in path:
                print(path)
                os.remove(path)
            else:
                f = open(path, "r")
                print(path)
                try:
                    lines = json.loads(f.read())   
                except UnicodeDecodeError as e:
                    print(f"Unicode decoding error: {e}")
                messagesList.append(lines)
                with open(file_path, "w") as file:
                    file.write(lines)
    print(messagesList)
    print(f"File '{file_path}' created with specified content.")

directory = 'messages'
messagesList = []
file_path = "allMessages.json"
CreateFilterDiscord(directory, messagesList, file_path)