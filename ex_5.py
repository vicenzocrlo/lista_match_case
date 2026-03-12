while True:

    print("\nVamos traduzir sua cor?\n")
    cor = input("Digite a sua escolha de cor em português (vermelho, azul, verde, amarelo): ")

    match cor:
        case "vermelho":
             print("The translation of vermelho is red")
        case "azul":
            print("The translation of azul is blue")
        case "verde":
            print("The translation of verde is green")
        case "amarelo":
            print("The translation of amarelo is yellow")
        case "sair":
            print("Saindo...")
            break

        case _:
            print("Opção invalida! Tente novamente...")

