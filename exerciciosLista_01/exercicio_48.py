sm = float(input("\nEntre como o salário mínimo: "))
qtdade = float(input("\nEntre com a quantidade de quilowhatt: "))
preco = sm / 700
vp = preco * qtdade
vd = vp * 0.9
print(f"\nPreço do quilowhatt: {preco:.2f}, \nValor a ser pago: {vp:.2f}")
print(f"\nValor com desconto:{vd:.2f}")
print("\n")