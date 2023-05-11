import nlpcloud

client = nlpcloud.Client("nllb-200-3-3b", "3c1bbe039a3df4fc8ebc3025dfd5aabd63767091")

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

receive_text = receive_text_input()
response_text = client_output(receive_text)

def save_receive_text(input_text):
    file = open("translations.txt", "a")
    file.write("Entrada: " + input_text + "\n")
    file.close()

def save_response_text(output_text):
    if output_text:
        file = open("translations.txt", "a")
        file.write("Tradução: " + output_text + "\n\n")
        file.close()

save_receive_text(receive_text)
save_response_text(response_text)