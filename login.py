from connection_mongo import *
from create_user import *

def ask_user():
    username = input("Informe seu nome de usuário: ")
    if username in collection_users:
        return username
    else:
        create_user(create_username(), create_password())

# def ask_password(username):
#     username = ask_user()
#     password = (input("Informe sua senha: "))
#     if collection_users.count_documents({"user" : username}):
        