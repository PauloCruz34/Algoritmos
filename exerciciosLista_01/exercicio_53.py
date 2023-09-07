a = float(input("\n Digite a base do paralelepipedo: "))
b = float(input("\n Digite a altura do paralelepipedo: "))
c = float(input("\n Digite a profundidade do paralelepipedo: "))
import math as m
diagonal = m.sqrt(a**2 + b**2 + c**2)
print(f"\n Diagonal = {diagonal:.2f}")
print("\n")