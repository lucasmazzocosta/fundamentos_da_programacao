print(" ---Bem-vindo(a) ao Caixa Registradora de Mercado")
valores = []

while True:
    preco_produto = float(input("Digite o valor do preço do produto: "))
    
    if preco_produto == 0:
        break
    
    valores.append(preco_produto)

print(f"Quantidade total de produtos: {len(valores)}")
print(f"Valor total da compra: {sum(valores):.2f}")
print("Encerrando...")