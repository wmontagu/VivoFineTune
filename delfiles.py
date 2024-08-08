import os
import pandas as pd
import random
import math
def delChannels():
    directory = 'messages'
    for d in os.listdir(directory):
        subdir = os.path.join(directory, d)
        for filename in os.listdir(subdir):
            path = os.path.join(subdir, filename)
            if "channel" in path:
                print(path)
                os.remove(path)

def filter(directory, date, messageLength):
    messagesContents = []
    for d in os.listdir(directory):
        subdir = os.path.join(directory, d)
        for filename in os.listdir(subdir):
            path = os.path.join(subdir, filename)
    return messages


