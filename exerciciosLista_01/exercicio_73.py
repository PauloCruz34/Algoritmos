num = float(input("\n Digite um número com parte fracionada: "))
numi = int(num)
numfrac = num - numi
numa = int(num+0.00001)
print(f"\n Parte inteira: {numi}")
print(f"\n Parte fracionada {numfrac + 0.00001:.3f}")
print(f"\n Número arredondado : {numa}")
print("\n")