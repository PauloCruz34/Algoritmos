'''Uma pessoa muito organizada gostaria de fazer um algoritmo para armazenar os 
seguintes dados de um talonário após a utilização total do mesmo: n2do cheque, 
valor, data e destino. Sabendo-se que o número de cheques pode ser variável e 
não ultrapassa 20, construa esse algoritmo de tal maneira que possa gerar um relatório no vídeo.''' 

# Número máximo de cheques
MAX_CHEQUES = 20

# Inicialize listas para armazenar os dados
num = [None] * MAX_CHEQUES
valor = [None] * MAX_CHEQUES
destino = [None] * MAX_CHEQUES
data = [None] * MAX_CHEQUES

# Obtenha o número de cheques do talonário
nc = int(input("Número de cheques do talonário: "))

# dados dos cheques
for k in range(nc):
    num[k] = input("Número do cheque: ")
    valor[k] = input("Valor do cheque: ")
    data[k] = input("Data do cheque (ddmmaa): ")
    destino[k] = input("Destino do cheque: ")

# relatório dos cheques
print("\nRELACAO dos CHEQUES\n")
for k in range(nc):
    print(f"Numero do cheque: {num[k]}")
    print(f"Valor do cheque: {valor[k]}")
    print(f"Data do cheque: {data[k]}")
    print(f"Destino do cheque: {destino[k]}\n")
    input("Pressione Enter para ver outro cheque: ")

print("\nFim do relatório")
