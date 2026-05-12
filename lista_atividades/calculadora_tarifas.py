# print(" ---Bem-vindo(a) a Calculadora de Tarifas--- ")
# valor_gasto = int(input("Digite o valor gasto em kWh: "))

# if valor_gasto < 0:
#      print('Valor Inválido, repita novamente o processo.')
# elif valor_gasto > 0 and valor_gasto <= 100:
#      print(f'Seu consumo foi de: {valor_gasto}')
#      print('Sua taxa de tarifa foi de R$0,40.')
#      print(f'Valor total a pagar: {valor_gasto * 0.4}')
# elif valor_gasto > 101 and valor_gasto <= 200:
#      print(f'Seu consumo foi de: {valor_gasto}')
#      print('Sua taxa de tarifa foi de R$0,60.')
#      print(f'Valor total a pagar: {valor_gasto * 0.6}')
# elif valor_gasto > 200:
#      print(f'Seu consumo foi de: {valor_gasto}')
#      print('Sua taxa de tarifa foi de R$0,90.')
#      print(f'Valor total a pagar: {valor_gasto * 0.9}')
# else:
#      print("Digite um valor válido!")

# print("Encerrando...")




# Declaração das variáveis globais - snake case
valor_ate_100kw = 0.4
valor_ate_200kwh = 0.6
valor_acima_200kwh = 0.9

print(f" ------ Seja Bem-vindo ao Programa de Cálculo de Energia Elétrica ------")

while True:
    input_kwh = input(f"Digite a quantidade de kwh consumidos(ou 'sair' para encerrar): ")
    if input_kwh.lower() == "sair":
        print("👋 Encerrando o programa. Obrigado por usar!\n")
        break
    elif not input_kwh.isdigit():
        print("❌ Entrada Inválida! Por favor digite um número válido ou 'sair' para encerrar\n")
        continue
    else:
        kwh = int(input_kwh)
        if kwh <= 100:
            valor_total = kwh * valor_ate_100kw
            print(f"📈 A faixa de consumo é: 0 a 100 kwh.")
            print(f"💰 O valor total da conta de energia é: R${valor_total:.2f}\n")
        elif kwh <= 200:
            valor_total = 100 * valor_ate_100kw + (kwh - 100) * valor_ate_200kwh
            print(f"📈 A faixa de consumo é: entre 100 a 200 kwh.")
            print(f"💰 O valor total da conta de energia é: R${valor_total:.2f}\n")
        else: 
            valor_total = 100 * valor_ate_100kw + 100 * valor_ate_200kwh + (kwh - 200) * valor_acima_200kwh
            print(f"📈 A faixa de consumo é: entre 200kwh ou mais.")
            print(f"💰 O valor total da conta de energia é: R${valor_total:.2f}\n")