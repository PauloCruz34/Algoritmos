import math as m
x = float(input("\n Digite o valor de x: "))
if x > 4 or x < -4 :
    fx = (5 * x + 3)/ m.sqrt(x**2 - 16)    
    print(f"\n f(x)= {fx}")
else:
    print("\n Não pode ser feita")
print("\n")

    