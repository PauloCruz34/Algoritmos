MAX_CLIENTES = 50
op = 0
c = 0
dados1 = [None] * MAX_CLIENTES
dados2 = [None] * MAX_CLIENTES
dados3 = [None] * MAX_CLIENTES
milha = [0.0] * MAX_CLIENTES

while op != 6:
    print("********************")
    print(" * MENU *")
    print("********************")
    print("1 - Cadastrar dados do cliente")
    print("2 - Cadastrar milhagem do cliente")
    print("3 - Listar milhagem do cliente")
    print("4 - Imprimir nomes com maior e menor milhagem")
    print("5 - Imprimir nomes e milhagens")
    print("6 - SAIR")
    op = int(input("OPÇÃO: "))

    if op == 1:
        if c < MAX_CLIENTES:
            print(f"{c + 1} - Nome: ", end="")
            dados1[c] = input()
            print("Endereço: ", end="")
            dados2[c] = input()
            print("Telefone: ", end="")
            dados3[c] = input()
            c += 1
        else:
            print("Arquivo cheio")

    elif op == 2:
        print("Nome para procurar: ", end="")
        nome = input()
        d = 0
        while d < c - 1 and nome != dados1[d]:
            d += 1
        if nome == dados1[d]:
            print(f"Digite milhagem de {dados1[d]}: ", end="")
            milhas = float(input())
            milha[d] -= milhas
        else:
            print("Nome não encontrado")

    elif op == 3:
        print("Nome para procurar: ", end="")
        nome = input()
        d = 0
        while d < c - 1 and nome != dados1[d]:
            d += 1
        if nome == dados1[d]:
            print(f"Milhagem de {dados1[d]}: {milha[d]}")
        else:
            print("Não encontrado")

    elif op == 4:
        d = 1
        posmenor = 0
        posmaior = 0
        while d < c:
            if milha[d] > milha[posmaior]:
                posmaior = d
            else:
                if milha[d] < milha[posmenor]:
                    posmenor = d
            d += 1

        print("Dados da pessoa de maior milhagem")
        print(f"Nome: {dados1[posmaior]}")
        print(f"Endereço: {dados2[posmaior]}")
        print(f"Telefone: {dados3[posmaior]}")
        print(f"Milhagem: {milha[posmaior]}\n")
        print("Dados da pessoa de menor milhagem")
        print(f"Nome: {dados1[posmenor]}")
        print(f"Endereço: {dados2[posmenor]}")
        print(f"Telefone: {dados3[posmenor]}")
        print(f"Milhagem: {milha[posmenor]}")

    elif op == 5:
        print("Listagem")
        for d in range(c):
            print(f"{d + 1} - {dados1[d]}: {milha[d]}")

    elif op == 6:
        print("BOA VIAGEM")

    else:
        print("Opção inexistente")
