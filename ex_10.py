while True:
    menu = """ \n
    ==========SISTEMA DE PAGAMENTO==========
    
    Escolha a sua forma de pagamento abaixo

    [1]\tDébito
    [2]\tCrédito
    [3]\tPix
    [5]\tSair

    """
    print(menu)
    opcao = int(input("Digite a sua opção aqui: "))

    match opcao:
        case 1:
            print("A opção de pagamento em débito não oferece descontos ou acréscimos, o valor é o mesmo.")

        case 2:
            print("A opção de pagamento em crédito oferece um acréscimo no valor, por conta da taxa do banco.")
        case 3:
            print("A opção de pagamento em pix oferece um desconto.")