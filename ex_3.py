while True:
    menu = """ \n
    ==========SISTEMA DE LOGIN========== 

    Digite o seu nome de usuário com base nos listados abaixo
    
    "Admin"
    "Professor"
    "Aluno"

    Caso deseja sair digite "sair"
    """
    print(menu)
    user = input("Digite aqui:\n ")
    
    match user:
        case "Admin":
            senha = input("Usuários com permissão total necessitam de senha, digite a senha de Admin:\n ")
            if senha == "toor":
                print("Seja bem vindo! Você fez login com sucesso a sua conta de Admin.\n")
            else:
                print("Senha incorreta, tente novamente.\n")

        case "Professor":
            print("Seja bem vindo! Você fez login com sucesso a sua conta de Professor. Acesso restrito ao Ambiente acadêmico\n")

        case "Aluno" :
            print("Seja bem vindo! Você fez login com sucesso a sua conta de Aluno. Acesso restrito ao ambiente de estudos\n")

        case "sair" :
            print("Saindo...\n")
            break

        case _:
            print("Opção inválida, tente novamente\n")




