import math as m

b = float(input("\n Digite a base do retângulo: "))
h = float(input("\n Digite a altura do retângulo: "))
perimetro = 2*(b + h)
area = b * h
diagonal = m.sqrt(b**2 + h**2)
print(f"\n Perimetro = {perimetro}")
print(f"\n Área = {area}")
print(f"\n Diagonal = {diagonal:.2f}")
print("\n")
