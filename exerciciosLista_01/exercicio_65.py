import math as m
altura = float(input("\n Digite a altura da lata: "))
raio = float(input("\n Digite o raio da lata: "))
volume = m.pi * raio**2 * altura
print(f'\n O volume da lata é : {volume:.2f}')
print("\n")
