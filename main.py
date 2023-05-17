from connection_mongo import *
from translate import *
from date_time import *
from login import *

login = check_password(check_user())

if login == True:
    receive_text = receive_text_input()
    response_text = client_output(receive_text)

    collection_logs = clientMongo["translation_archives"]["logs"]

    if collection_logs.insert_many([{"input" : receive_text, 
                                     "output" : response_text, 
                                     "date-time" : {"date" : current_day, "time" : current_time}}]):
        print("Tradução registrada com sucesso!")
        print(f'Sua tradução: {response_text}')                       