peso = float(input("\n Digite seu peso:"))
alt = float(input("\n Digite sua alt: "))
imc = peso / alt**2
if imc < 20:
    print("\n Abaixo do peso.")
elif imc <= 25:
    print("\n Normal.")
elif imc <= 30:
    print("\n Sobrepeso.")
elif imc <= 35:
    print("\n Obeso.")
else:
    print("\n Obesidade mórbida.")
print("\n")