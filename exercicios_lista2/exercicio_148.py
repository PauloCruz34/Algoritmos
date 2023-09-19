op = int(input("\n Digite 1 para região Norte, 2-Nordeste, 3- Centro Oeste e 4 para Sul: "))
iv = int(input("\n Digite 1 para ida e 2 para volta: "))
if op == 1:
    if iv == 1:
        print(f"\n O valor da passagem de ida para o note é R$ 500,00")
    else:
        print("\n O valor de ida e volta para a R. Norte é R$ 950,00")
elif op == 2:
    if iv == 1:
        print("\n O valor da passagem de ida para o Nordeste é R$ 350,00")
    else:
        print("\n O valor de ida e volta para o Nordeste é R$ 650,00")
elif op == 3:
    if iv == 1:
        print("\n O valor da passagem de Ida para a R. Centro Oeste é R$ 350,00")
    else:
        print("\n O valor de ida e volta para a R. Centro Oeste é R$ 600,00")
elif op == 4:
    if iv ==1:
        print("\n O valor da passagem de Ida para a R. Sul é R$ 300,00")
    else:
        print("\n O valor de ida e volta para a R. Sul é R$ 550,00")
else:
    print("\n Opção inválida")