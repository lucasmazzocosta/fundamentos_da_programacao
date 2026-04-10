idade = int(input('Digite sua idade: '))

if idade < 24:
	print('Entrada não autorizada pela idade')
elif idade >= 24:
	cadastro_shopping = input('Digite se você é cadastrado (sim ou não): ')
	if cadastro_shopping == 'não':
		print('Entrada não autorizada por falta de cadastro!')
	elif cadastro_shopping == 'sim':
		tipo_veiculo = input('Digite se o seu veículo é grande ou pequeno: ')
		cliente_vip = input('Você é vip (sim ou não): ')
		if tipo_veiculo == 'grande' and cliente_vip == 'sim':
			print('Entrada autorizada!!')
		elif cliente_vip == 'sim' and tipo_veiculo == 'pequeno':
			print('Entrada autorizada!')
		elif cliente_vip == 'não':
			print('Entrada não autorizada!')