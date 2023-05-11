from connection_mongo import *
from create_user import *

def ask_user():
    username = input("Informe seu nome de usuário: ")
    if username in collection_users:
        return username

# Continuar checagem de senha
# def ask_password():
#     password = (input("Informe sua senha: "))
#     if password in collection_users