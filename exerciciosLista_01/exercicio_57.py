pr1 = float(input("\n Digite PR-1: "))
pr2 = float(input("\n Digite PR-2: "))
mf = (pr1 + pr2) / 2
print(f'\n Média Truncada = {int((mf - 0.5) + 0.001)}')
print(f'\n Média Arredondada = {int(mf + 0.001)}')
print('\n')