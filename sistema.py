usuarios = {
    "romulo": "senha123",
    "ana": "senha456",
    "joao": "senha789"
}

def autenticar_usuario():
    print("Bem-vindo ao sistema de login!")

    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")

    if usuario in usuarios and usuarios[usuario] == senha:
        print(f"Login bem-sucedido, {usuario}!")
    else:
        print("Usuário ou senha incorretos. Tente novamente.")


autenticar_usuario()
