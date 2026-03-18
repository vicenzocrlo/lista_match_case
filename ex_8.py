while True:
    menu = """ \n
    ==========PASSAGENS==========

    Seja bem vindo! Vamos reservar sua passagem?

    Escolha a passagem para o seu destino abaixo

    [1]\tSão Paulo  
    [2]\tRio de Janeiro 
    [3]\tCuritiba
    [4]\tSalvador
    [5]\tSair
    
    """

    print(menu)
    opcao = int("Digite aqui sua opção de escolha: ")

    match opcao:
        case 1:
            print("O valor da sua passagem de ida para São Paulo é 200 reais ")

        case 2:
            print("O valor da sua passagem de ida para o Rio de Janeiro é 300 reais")

        case 3:
            print("O valor da sua passagem de ida para Curitiba é 250 reais")

        case 4:
            print("O valor da sua passagem de ida para Salvador é 400 reais")

        case 5:
            print("Saindo...")
            break