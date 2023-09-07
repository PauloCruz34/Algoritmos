valor = float(input("\n Digite o valor da prestação: "))
taxa = float(input("\n Digite a taxa: "))
tempo = int(input("\n Digite o tempo em atraso: "))
prest = valor + (valor*(taxa/100) * tempo)
print(f'\n O valor da prestação em atraso é = {prest:.2f}')
print("\n")

