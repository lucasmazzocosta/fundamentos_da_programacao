while True:
    nome_pessoa = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    validacao_convite = input('Possui convite?(S/N): ')

    if idade < 16 or validacao_convite == 'N':
        print('Entrada negada!')
    elif idade >= 16 and validacao_convite == 'S': 
        print('Entrada permitida')
    else:
        ('Entrada negada!') 
    saida = input('Digite "sair" para encerrar: ')
    if saida == 'sair':
        print('Sistema encerrado!')
        break
    else: 
        print('Continuando o loop!')