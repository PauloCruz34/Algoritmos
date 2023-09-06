num = float(input("\nEntre com o logaritmo: "))
base = float(input("\nEntre com a base: "))
import math as m
log = m.log(num) / m.log(base)
print(f"\n O logaritmo de {num} na base {base} é {log:.2f}")
print("\n")
