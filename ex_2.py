while True:
    menu = """ \n
    ============CALCULADORA DE ÁREA============
    
    Escolha a figura geométrica que você deseja calcular a área
    
    [1]\tquadrado
    [2]\ttriângulo
    [3]\tretângulo
    [4]\tSair
    
    """
    print(menu)

    opcao = int(input("Digite a opção de figura que deseja calcular: "))

    match opcao:
        case 1:
            lado = float(input("Digite o valor de um dos lados do seu quadrado: "))
            area = lado ** 2
            print(f"O valor da área do seu quadrado é {area} cm")

        case 2:
            base= float(input("Digite o valor da base do seu triâgulo: "))
            altura = float(input("Digite o valor da altura do seu triângulo: "))
            area_2 = base * altura / 2
            print(f"O valor da área do seu triângulo é {area_2} cm")

        case 3:
            comprimento = float(input("Digite o valor do comprimento do seu triângulo: "))
            largura = float(input("Digite o valor da largura do seu retângulo: "))
            area_3 = comprimento * largura
            print(f"O valor da área do seu retângulo é {area_3} cm")
        case 4:
            print("Saindo...")
            break

        case _:
            print("Opção inválida, digite novamente.")