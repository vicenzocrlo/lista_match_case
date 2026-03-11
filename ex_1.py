
while True:
    menu = """ \n
    ===================CONVERSOR DE MOEDAS=====================

    Escolha a moeda que deseja converter para Real (BRL):

    [1]\tDólar(USD)
    [2]\tEuro(EUR)
    [3]\tLibra(GBP)
    [4]\tSair

    """

    print(menu)

    opcao = int(input("Digite sua opção de conversão: "))

    match opcao:
        case 1:
            dolar = float(input("Digite o valor em dólar: "))
            valor = dolar * 5.20
            print(f"Você tem um total de {valor} reais.")

        case 2:
            euro = float(input("Digite o valor em euro: "))
            valor_2 = euro * 6.00
            print(f"Você tem um total de {valor_2} reais.")

        case 3:
            libra = float(input("Digite o valor em libras: "))
            valor_3 = libra * 7.00
            print(f"Você tem um total de {valor_3} reais.")

        case 4:
            print("Saindo...")
            break

        case _:
            print("Opção invalida, tente novamente.")







