from connection_mongo import *
from create_user import *

def check_user():
    username = input("Informe seu nome de usuário: ")
    user_document = collection_users.find_one({"user" : username})
    print(user_document)
    if user_document is not None:
        return username
    else:
        while True:
            check_yn = input("Ao que parece você ainda não tem um cadastro. Gostaria de realizá-lo (S/N)? ")
            if check_yn.lower() == "s":
                create_user(create_username(), create_password())
                print("Agora, faça login para utilizar o programa.")
                quit()
            elif check_yn.lower() == "n":
                print("Certo, você não será cadastrado.")
                quit()
            else:
                print("Opção inválida. Por favor, informe S para sim ou N para não.")

def check_password(username):
    while True:
        password = input("Informe sua senha: ")
        user_document = collection_users.find_one({"user" : username})
        if user_document is not None and user_document["password"] == password:
            print("Login realizado com sucesso.")
            return True
        else:
            print("Senha incorreta.")



        