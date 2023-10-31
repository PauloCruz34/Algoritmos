#Criar um algoritmo que armazene 10 números em um vetor. Na entrada de dados, o número já deverá ser armazenado na sua posição definitiva em ordem decrescente. Imprimir o vetor logo após a entrada de dados.

a = [0] * 10


for L in range(10):
    n = int(input(f"Elemento do vetor A[{L}]: "))
    c = 0
    while c < L and n > a[c]:
        c += 1
    if L > 0:
        for d in range(L, c, -1):
            a[d] = a[d - 1]
    a[c] = n


print("\nVetor Ordenado\n")
for L in range(10):
    print(f"a[{L + 1}] - {a[L]}")
