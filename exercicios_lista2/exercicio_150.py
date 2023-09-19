import math as m
ang =  float(input("\n Digite o ângulo em graus: "))

rang =  ang * m.pi/180
if rang > m.pi/2 and rang <= m.pi or rang > 3 * m.pi / 2 and 2 * m.pi:
    print(f"\n seno: {m.sin(rang)}")
else:
    print(f'\n co -seno : {m.cos(rang)}')
print("\n")