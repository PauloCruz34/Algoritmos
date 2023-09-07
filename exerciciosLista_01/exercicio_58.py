import math as m
xnum1 = float(input("\n Digite um número"))
xnum2 = float(input("\n Digite outro número"))
xnum3 = float(input("\n Digite outro número"))

x = xnum1 + xnum2 / (xnum3 + xnum1) + 2*(xnum1 - xnum2) + m.log(64) / m.log(2)
print(f"\n X = {x:.2f}")
print("\n")