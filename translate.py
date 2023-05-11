from connection_nlpcloud import *
from connection_mongo import *
from create_user import *

def receive_text_input():
    text = input("Informe um texto: ")
    if len(text) > 400:
        print("O texto deve ter, no máximo, 400 caracteres.")
        quit()
    else: 
        return text

def client_output(input_text):
    response = client.translation(input_text, source='por_Latn', target='eng_Latn')
    for value in response.values():
        return str(value)

create_user(username_input, password_input)

receive_text = receive_text_input()
response_text = client_output(receive_text)

translation_archives = clientMongo["translation_archives"]
collection_logs = translation_archives["logs"]
collection_logs.insert_many([{"input" : receive_text, "output" : response_text}])