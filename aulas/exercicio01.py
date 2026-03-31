idade = int(input('Digite sua idade: '))

if idade >= 18:
    salario = int(input('Digite seu salario: '))
    if salario >= 2000 and salario < 5000:
       tempo_anos = int(input('Digite o tempo de trabalho (em anos): '))
       if tempo_anos < 2:
        print('Seu empréstimo foi negado!')
       else:
          valor_emprestimo = int(input('Digite o valor do empréstimo: '))
          parcela = valor_emprestimo / (12 * tempo_anos)
          if valor_emprestimo / 100 > parcela * 0.30:
             print('Seu empréstimo foi aprovado!')
             print(f'O cliente tem {idade} anos, salário de R$ {salario} e {tempo_anos} anos de trabalho - todas as condições foram atendidas, portanto o empréstimo é aprovado')
          else: 
             print('Seu empréstimo foi negado')
    elif salario < 2000:
       print('Seu empréstimo foi negado!') 
    else:
        print('Seu empréstimo foi aprovado!')
else:
    print('Seu empréstimo foi negado!')