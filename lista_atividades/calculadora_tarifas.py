print(" ---Bem-vindo(a) a Calculadora de Tarifas--- ")
valor_gasto = int(input("Digite o valor gasto em kWh: "))

if valor_gasto < 0:
     print('Valor Inválido, repita novamente o processo.')
elif valor_gasto > 0 and valor_gasto <= 100:
     print(f'Seu consumo foi de: {valor_gasto}')
     print('Sua taxa de tarifa foi de R$0,40.')
     print(f'Valor total a pagar: {valor_gasto * 0.4}')
elif valor_gasto > 101 and valor_gasto <= 200:
     print(f'Seu consumo foi de: {valor_gasto}')
     print('Sua taxa de tarifa foi de R$0,60.')
     print(f'Valor total a pagar: {valor_gasto * 0.6}')
elif valor_gasto > 200:
     print(f'Seu consumo foi de: {valor_gasto}')
     print('Sua taxa de tarifa foi de R$0,90.')
     print(f'Valor total a pagar: {valor_gasto * 0.9}')
else:
     print("Digite um valor válido!")

print("Encerrando...")