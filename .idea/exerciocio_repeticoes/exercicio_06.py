# Dizemos que um número natural é triangular se ele é produto de três números naturais
#consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n,
#verificar se N é triangular.

n = int(input("informe o valor inteiro a ser analisado: "))

calculo_nr_triangular = 0
y=1

while calculo_nr_triangular < n:
    calculo_nr_triangular = y*(y+1)*(y+2)
    y = y + 1
if calculo_nr_triangular == n:
    print(f"é triangular")
else:
    print(f"O numero não é triangular")
