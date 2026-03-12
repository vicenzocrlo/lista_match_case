while True:
    menu = """ \n
    ==========ATENDIMENTO TELEFÓNICO==========

    Seja bem vindo! Como podemos te ajudar?
    
    Escolha uma opção abaixo para receber ajuda

    [1]\tSuporte Técnico
    [2]\tFinanceiro
    [3]\tCancelamento
    [4]\tFalar com um atendente
    [5]\tSair

    """

    menu_cancelamento = """ \n
    ==========CANCELAMENTO==========
        
    Nos ajude a melhorar, qual foi o problema que te motivou a realizar o cancelamento?
     
    Escolha uma opção abaixo:
    
    [1]\tInstabilidade
    [2]\tCusto Elevados
    [3]\tFalhas no Suporte
    [4]\tMal Funcionamento
    [5]\tOutros
    [6]\tVoltar
        
    """
    print(menu)

    opcao = int(input("Digite a sua opção de atendimento: "))

    match opcao:
        case 1:
            print("Entrando em contato com a equipe de Suporte Técnico...")

        case 2:
            print("Entrando em contato com a equipe do financeiro...")
        case 3:
           print(menu_cancelamento)
           cancel = int(input("Digite sua opção: "))

           if cancel == 1:
                print("Obrigado pelo seu Feedback!Realizando o cancelamento...")
                break
           elif cancel == 2:
                print("Obrigado pelo seu Feedback!Realizando o cancelamento...")
                break
           elif cancel == 3:
                print("Obrigado pelo seu Feedback!Realizando o cancelamento...")
                break
           elif cancel == 4:
                print("Obrigado pelo seu Feedback!Realizando o cancelamento...")
                break
           elif cancel == 5:
                outro = input("Qual foi o motivo em questão que te levou ao cancelamento?: ")
                print("Obrigado pelo seu Feedback! Realizando o cancelamento...")
                break

           elif cancel == 6:
                print("Voltando para o processo de atendimento...")

           else:
                    print("Opção invalida, tente novamente!")

        case 4:
            print("Entrando em contato com algum Atendente...")

        case 5:
            crtz = input("Você realmente deseja sair do sistema?(S ou N): ")
            if crtz == "S":
                print("Saindo do sistema...")
                break

            elif crtz == "N":
                print("Voltando para o processo de atendimento...")

            else:
                print("Opção invalida, tente novamente!")

        case _:
            print("Opção inválida, tente novamente!")


