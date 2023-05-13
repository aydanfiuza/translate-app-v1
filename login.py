from connection_mongo import *
from create_user import *

def check_user():
    username = input("Informe seu nome de usuário: ")
    user_document = collection_users.find_one({"user": username})
    if user_document is not None:
        return username
    else:
        while True:
            check_yn = input("Ao que parece você ainda não tem um cadastro. Gostaria de realiza-lo (S/N)? ")
            if check_yn == "S" or check_yn == "s":
                create_user(create_username(), create_password())
            elif check_yn == "N" or check_yn == "n":
                print("Certo, você não será cadastrado.")
                quit()
            else:
                print("Opção inválida. Por favor, informe S para sim ou N para não.")

def check_password(user):
    while True:
        password = (input("Informe sua senha: "))
        user_document = collection_users.find_one({"user": user})
        if user_document is not None and user_document["password"] == password:
            print("Login realizado com sucesso.")
            return True
        else:
            print("Senha incorreta.")



        