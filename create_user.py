from connection_mongo import *

def create_username():
    username = input("Crie seu nome de usuário: ")
    return username

def create_password():
    password = input("Crie sua senha: ")
    if len(password) < 8:
        print("A senha deve ter mais de 8 caracteres.")
        quit()
    else:
        return password

username_input = create_username()
password_input = create_password()
user = clientMongo["user"]
collection_users = user["users"]

def create_user(username, password):
    if collection_users.insert_many([{"user" : username, "password" : password}]):
        print("Usuário cadastrado com sucesso.")
