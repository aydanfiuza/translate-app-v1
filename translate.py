from connection_nlpcloud import *

def receive_text_input():
    while True:
        text = input("Insira o texto que será traduzido: ")
        if len(text) > 400:
            print("O texto deve ter, no máximo, 400 caracteres.")
        else: 
            return text


def client_output(input_text):
    response = client.translation(input_text, source='por_Latn', target='eng_Latn')
    for value in response.values():
        output = str(value)
    return output