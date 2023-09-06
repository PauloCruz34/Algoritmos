num = int(input("\nEntre com um número de 3 dígitos: "))
c = num // 100 # divisao inteira por 100
d = num % 100 // 10 #pega o resto da divisao por 100 e divisao inteira por 10
u = num%10 #resto da divisao por 10
num1 = u*100 + d*10 + c
print(f"\nNúmero: {num}")
print(f"\nNúmero invertido: {num1}")
print("\n")