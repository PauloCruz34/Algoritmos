
#Armazenar 15 números inteiros em um vetor NUM e imprimir uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.

num = [0] * 15
for L in range(15):
    num[L] = int(input(f"Digite o {L + 1} número: "))
print("\nRELACAO DOS NUMEROS\n")
for L in range(15):
    print(f"{L + 1} - {num[L]}", end=' ')
    if num[L] % 2 == 0:
        print("e' PAR")
    else:
        print("e' IMPAR")
