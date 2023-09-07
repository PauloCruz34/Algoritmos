na = int(input("\n Entre com as horas trabalhadas: "))
vha = float(input("\n Valor hora-aula: "))
pd = float(input("\n Percentual de descont: " ))
sb = na * vha
td = (pd / 100)*sb
sl = sb - td
print(f"Salario liquido: {sl:.2f}")
print("\n")
