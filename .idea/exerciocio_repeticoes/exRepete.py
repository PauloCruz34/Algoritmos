fim = int(input("\nDigite um numero: "))
x = 0
while x <= fim:
    if x % 2 == 1:
        print(x)
    x = x  + 1
    
for tabuada in range(1,11):
    print("\nTabuada do ", tabuada)
    for i in range(1,11):
        print(tabuada, " x ", i, " = ", tabuada * i)
        
lista = [23,35,36,78,98]
for x in lista:
    print(x)
    
dict_elementos = {"a":23, "b": 56}
for elementos in dict_elementos:
    print (elementos)
    