nome = input("\n Digite seu nome: ")
idade = int(input("\n Digite sua idade: "))
if idade <= 10:
    print(f"{nome} pagará R$ 30,00")
elif idade <= 29:
    print(f"{nome} pagara R$ 60,00")
elif idade <= 45:
    print(f"{nome} pagara R$ 120,00")
elif idade <= 59:
    print(f"{nome} pagara R$ 150,00")
elif idade <= 65:
    print(f"{nome} pagara R$ 250,00")
else:
    print(f"{nome} pagara R$ 400,00")
print("\n")
    
      
    
