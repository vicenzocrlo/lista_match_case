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
    print(menu)
    opcao = int(input("Digite a sua opção de atendimento: "))

    match opcao:
        case 1:
            print("Entrando em contato com o suporte técnico...")
