p = float(input("\n Digite o valor da aplicação: "))
i = float(input("\n Digite o valor da taxa(0-1): "))
n = int(input("\n Digite o número de meses: "))
va = p*(((1+i)**n)-1)/i
print(f"\n O valor acumulado sera : R${va}")
print('\n')