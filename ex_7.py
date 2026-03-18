while True:
    menu = """ \n
    ==========CALULADORA SIMPLES==========

    Seja bem vindo! Vamos calcular?
    
    Escolha uma opção abaixo 

    [1]\tSoma
    [2]\tSubtração
    [3]\tMultiplicação
    [4]\tDivisão
    [5]\tSair

    """

    print(menu)
    opcao = int(input("Digite a sua opção de escolha: "))

    match opcao:
        case 1:
            num_1 = float(input("Digite o seu primeiro número: "))
            num_2 = float(input("Digite o seu segundo número: "))
            soma = (num_1 + num_2)
            print(f"\nO resultado da sua soma é {soma}")
        case 2:
            num_3  = float(input("Digite o seu primeiro número: "))
            num_4  = float(input("Digite o seu segundo número: "))
            sub = (num_3 - num_4)
            print(f"\nO resultado da sua subtração é {sub}")
        case 3:
            num_5 = float(input("Digite o seu primeiro número: "))
            num_6 = float(input("Digite o seu segundo número: "))
            mult = (num_5 * num_6)
            print(f"\nO resultado da sua multiplicação é {mult}")
        case 4:
            num_7 = float(input("Digite o seu primeiro número: "))
            num_8 = float(input("Digite o seu segundo número: "))
            div = (num_7 / num_8)
            print(f"\nO resultado da sua divisão é {div}")
        case 5:
            print("\nSaindo...")
            break