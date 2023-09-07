deposito =  float(input("\n Digite o valor do  depósito: "))
taxa = float(input("\n Digite o valor da taxa: "))
valor = deposito * taxa/100
total = valor + deposito
print(f"\n Rendimentos = {valor}, Total = {total}")
print("\n")
