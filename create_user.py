from connection_mongo import *

def create_username():
    username = input("Crie seu nome de usuário: ")
    return username

def create_password():
    while True:
        password = input("Crie sua senha: ")
        if len(password) < 8:
            print("A senha deve ter no mínimo 8 caracteres.")
        else:
            return password

collection_users = clientMongo["user"]["users"]

def create_user(username, password):
    user_data = {"user": username, "password": password}
    if collection_users.insert_one(user_data):
        print("Usuário cadastrado com sucesso.")