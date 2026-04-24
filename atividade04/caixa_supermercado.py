while True:
    produto = int(input('Digite o valor do produto: '))
    contador = 0
    total += produto
    if produto == 0:
        print('Saindo do loop!')
        break
    elif produto > 100:
        desconto = 0.10
        preco_desconto = produto - (produto * desconto)
        print("Produto com desconto")
    # else:
    #     print()
    #     break
contador += 1

print('Total: ', total)
print('Quantidade: ', contador)
print('Média: ', total/contador)
