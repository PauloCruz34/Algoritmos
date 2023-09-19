saldoMedio = float(input("\n Digite o Saldo medio:"))
if saldoMedio <= 500:
    credito = 0
elif saldoMedio > 500 and saldoMedio <= 1000:
    credito = saldoMedio * 0.3
elif saldoMedio > 1000 and saldoMedio <= 3000:
    credito = saldoMedio * 0.4
elif saldoMedio > 3000:
    credito = saldoMedio * 0.5
if saldoMedio != 0:
    print(f"\n Como seu saldo era de {saldoMedio} seu credito será de {credito}")
else:
    print(f"Como seu saldo era de {saldoMedio}, você não terá nenhum credito")
print("\n")    