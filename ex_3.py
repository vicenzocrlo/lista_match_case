while True:
    user = input("Digite o seu nome de usuário (Admin, Professor, Aluno): ")

    match user:
        case "Admin":
            print("Seja bem vindo! Você tem o acesso Total.")

        case "Professor":
            print("Seja bem vindo! Você tem acesso apenas ao Ambiente acadêmico")

        case "Aluno" :
            print("Seja bem vindo! Você tem acesso apenas ao ambiente de estudos")

        case "sair" :
            print("Saindo...")
            break

        case _:
            print("Opção inválida, Digite novamente")




