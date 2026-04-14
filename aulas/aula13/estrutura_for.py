# Contar de 1 até 5
# for numero in range(1, 6):
#     print(f'Eu sou o número {numero}')

# Exemplo de Tabuada -> 5
i = 5 # variável escopo global
for numero in range(1, 11):
    total = i * numero # variável escopo local
    print(f'5 x {numero} = {total}')