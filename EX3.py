'''Faça uma função que recebe a idade de uma pessoa em anos, 
meses e dias e retorna essa idade expressa em dias. 
Considere um ano = 365 dias e um mês = 30 dias.'''

def idade_dias():
    anos = int(input('Digite sua idade em anos: '))
    meses = int(input('Digite quantos meses passaram desde o seu aniverserio: '))
    dias = int(input('Digite quantos dias quebrados tem desde o dia do seu aniversario desse mes: '))
    print((anos * 365) + (meses * 30) + dias)
idade_dias()

