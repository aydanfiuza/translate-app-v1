from connection_mongo import *
from create_user import *

def ask_user():
    username = input("Informe seu nome de usuário: ")
    if username in collection_users:
        return username
    else:
        print("Este usuário já está cadastrado. Por favor, escolha outro.")
        quit()
        
# Continuar checagem de senha
# def ask_password():
#     password = (input("Informe sua senha: "))
#     if password in collection_users