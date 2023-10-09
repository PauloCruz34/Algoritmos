# Ler o valor da conta e o valor pago
valor_conta = int(input("Digite o valor da conta: "))
valor_pago = int(input("Digite o valor pago: "))

# Calcular o troco
troco = valor_pago - valor_conta

# Lista de notas disponíveis
notas = [50, 20, 10, 5, 2, 1]

# Calcular e exibir as notas necessárias
for nota in notas:
    quantidade_notas = troco // nota
    if quantidade_notas > 0:
        print(f"{quantidade_notas} nota(s) de R${nota}")
        troco %= nota
