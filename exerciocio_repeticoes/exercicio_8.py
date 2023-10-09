n = int(input("Digite um numero inteiro positivo:"))
div = 0
for x in range(1,n):
    if (n% x == 0):
        div += 1
if (div == 0):
    print(f"{n} é primo")
else:
    print(f'{n} não é primo')
    