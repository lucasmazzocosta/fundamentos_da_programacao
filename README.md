# Anotações de fundamentos da programação 

# Tipos de dados em python
1. string
2. number int
3. number float
4. boolean

# Operadores matemáticos - básicos
+ -> adição
- -> subtração
* -> multiplicação 
/ -> divisão

# Operadores Lógicos
and -> e -> Se duas condições forem verdadeiras, o resultado é verdadeiro.
or -> ou -> Se uma condição for verdadeira, o resultado é verdadeiro.
not -> não -> nega a condição, se for falso é verdadeiro e se for verdadeiro é falso.

# Métodos em python
1. print() -> exibe informações mo terminals
2. input() -> capturar uma informação no terminal

# Format em python

# Estrutura condicional
``if (se)`` -> Verifica se uma condição é true (verdadeira). Se for ele executa o código.
``elif (senão se)`` -> É usado para testar várias condições. Ele só executa se todas as condições anteriores forem falsas.
``else (senão)`` -> Executa o código se a condição if for false (falsa).

# Laços de repetição
É um recurso de programação que permite executar um conjunto de comando várias vezes. Também são chamados de Loop, Laços de repetição ou iteração.
`For` -> utilizamos quando sabemos quantas vezes queremos repetir algo.
Sintaxe:
for variável in range(inicio, fim):
    comandos

[range]() -> Método que aceita geração de números.
[inicio] ->  É inclusivo. é o primeiro número a ser usado.
[fim] -> É exclusivo. O número utilizado é o anterior a esse.

## Escopo das variáveis
`Escopo Local` -> A variável só é acessada dentro da estrutura que ela foi criada.
`Escopo Global` -> A variável pode ser acessada por todo mundo.

# Variações das variáveis 
Variável em memória -> É declarada quando você não pretende utilizar essa variável em outros cenários.
Variável contador -> É utilizada para uma lógica onde a repetição irá ser alterada.

`While` -> É utilizado quando não sabemos quantas vezes o programa vai repetir. Ele repete enquanto uma condição for verdadeira.
Sitaxe: 
while condição:
    comandos

# Conversão de tipos em Python
1. int() -> a gente vai incuir qual variável/dado que queremos converter para número inteiro.
2. float() -> a gente vai incuir qual variável/dado que queremos converter para número decimal.
3. str() -> a gente vai incuir qual variável/dado que queremos converter para texto.

# Boas Práticas
1. Qualquer variável em python utiliza o padrão de case snake_case ou recentemente o cammelCase.
2. Se você observar alguma estrutura tipo nome(), 90% de chance de ser uma função.
3. Python não tem constante, porém utilizamos o padrão case
UPPERCASE,para simular que aquela variável não pode ser alterada.