angulo = float(input("\nigite um angulo em graus: "))
import math as m
rang = angulo*m.pi/180
print(f"\nSeno: {m.sin(rang)}")
print(f'\nCo-seno: {m.cos(rang)}')
print(f'\nTangente: {m.tan(rang)}')
print(f"\nCo-secante: {1/ m.sin(rang)}")
print(f"\nSecante: {1/m.cos(rang)}")
print(f'\nCotangente: {1/m.tan(rang)}')
print("\n")


