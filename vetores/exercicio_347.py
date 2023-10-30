#Criar um algoritmo que entre com dez nomes e imprima uma listagem contendo todos os nomes. 

nomes = []
for i in range(10):
    nome = input(f"Digite o {i + 1}º nome: ")
    nomes.append(nome)
print("\n Nomes digitados:")
for nome in nomes:
    print(nomes)