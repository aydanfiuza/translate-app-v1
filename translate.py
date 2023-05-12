from connection_nlpcloud import *
from connection_mongo import *
from create_user import *
from datetime import *

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

current_day = str(date.today())
time_now = datetime.now()
current_time = time_now.strftime("%H:%M:%S")

translation_archives = clientMongo["translation_archives"]
collection_logs = translation_archives["logs"]
log_id = collection_logs.count_documents({}) + 1

collection_logs.insert_many([{"_id" : log_id,
                              "input" : receive_text, 
                              "output" : response_text, 
                              "date-time" : {"date" : current_day, "time" : current_time}}])