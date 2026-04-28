print("---Bem-vindo ao Sistema de Gereciamento de Notas---")

alunos_cadastrados = int(input("Digite quantos alunos vão ser cadastrados: "))

notas_alunos = []
lista_nomes = []
situacao_aluno = []
contador = 0

while contador < alunos_cadastrados:
    nome_aluno = input("Digite o nome do aluno: ")
    lista_nomes.append(nome_aluno)

    nota01 = float(input("Digite a primeira nota: "))
    notas_alunos.append(nota01)
    
    nota02 = float(input("Digite a segunda nota: "))
    notas_alunos.append(nota02)
    
    nota03 = float(input("Digite a terceira nota: "))
    notas_alunos.append(nota03)

    media_notas = sum(notas_alunos) / len(notas_alunos)

    if media_notas >= 7:
        situacao_aluno.append("Aprovado")
    elif media_notas >= 5 and media_notas < 7:
        situacao_aluno.append("Recuperação")
    elif media_notas < 5:
        situacao_aluno.append("Reprovado") 

    contador += 1

print(f"Nome dos alunos: {lista_nomes}")
print(f"Notas dos alunos: {notas_alunos}")
print(f"Média das notas: {media_notas:.2f}")
print(f"Situação de cada aluno: {situacao_aluno}")
print("Finalizando...")