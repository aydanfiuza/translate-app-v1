import nlpcloud
import json

with open('apiConnection.json') as file:
    data = json.load(file)

client = nlpcloud.Client("nllb-200-3-3b", data["key"])