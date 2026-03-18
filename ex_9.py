while True:
    menu = """ \n
    ==========LOJA ONLINE ROUPAS==========

    Seja bem vindo! Como posso te ajudar hoje?

    Escolha a sua opção de compra e te informaremos o valor

    [1]\tCamisetas
    [2]\tCalças
    [3]\tMeias
    [4]\tBlusas de Frio
    [5]\tSair

    """
    print(menu)
    opcao = int(input("Digite a sua opção de escolha: "))

    match opcao:
        case 1:
            print("O valor em média das camisas é 60,00 reais.")

        case 2:
            print("O valor em média das calças é 120,00 reais.")
        case 3:
            print("O valor em média das meias é 20,00 reais.")
        case 4:
            print("O valor em média das Blusas de Frio é 160,00 reais")
        case 5:
            print("Saindo...")
            break
