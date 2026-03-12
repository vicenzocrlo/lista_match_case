while True:
    menu = """ \n
    ==========CALCULE SEU DESCONTO==========
    
    Escolha a categoria do produto que você deseja receber desconto
    
    [1]\tEletrônicos
    [2]\tRoupas
    [3]\tAlimentos
    [4]\tMóveis
    [5]\tOutros
    [6]\tSair
    
    """
    print(menu)

    opcao = int(input("Digite o número da sua categoria: "))

    match opcao:
        case 1:
            print("O percentual de desconto correspondende a Eletrónicos é 15% ")

        case 2:
            print("O percentual de desconto correspondende a Roupas é 20% ")

        case 3:
            print("O percentual de desconto correspondende a Alimentos é 10% ")

        case 4:
            print("O percentual de desconto correspondende a Móveis é 7%% ")

        case 5:
            outro = input("Digite o tipo do produto: ")
            preco = float(input("Digite o preço do produto: "))

            if preco < 30:
                print("O seu produto não pode receber desconto")

            elif preco > 30 and preco <= 60:
                print("O percentual de desconto do seu produto é 10%")

            else:
                print("O percentual de desconto do seu produto é igual a 15%")

        case 6:
            print("Saindo...")
            break

        case _:
            print("Opção invalida, tente novamente")

