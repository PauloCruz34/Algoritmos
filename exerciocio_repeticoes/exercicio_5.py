num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

while num2:
    num1, num2 = num2, num1 % num2

mdc = num1

print(f"O Máximo Divisor Comum (MDC) é: {mdc}")

