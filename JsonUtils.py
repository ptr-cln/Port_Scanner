import json

def extractJsonData(filename):
    with open(filename , "r") as file:
        data = json.load(file)
    return data