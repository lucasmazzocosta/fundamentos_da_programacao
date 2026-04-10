print('Sistema de Matrícula em Curso')

idade = int(input('Digite sua idade: '))

if idade < 18:
    print('Matrícula negada. Aluno menor de idade!')
elif idade >= 18:
    nota = float(input('Digite a sua nota: '))
    if nota >= 9:
        print('Matrícula aprovada automaticamente!')
    elif nota < 9:
        frequencia = int(input('Digite sua frequência: '))
        if (frequencia / 100) > 0.75:
            print('Matrícula aprovada!!')
        else:
            print('Matrícula negada')