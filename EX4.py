'''O código de César é uma das mais simples e conhecidas técnicas de criptografia. 
É um tipo de substituição na qual cada letra do texto e substituída por outra, 
que se apresenta no alfabeto abaixo dela um número fixo de vezes. 
Por exemplo, com uma troca de três posições, ‘A’ seria substituído 
por ‘D’, ‘B’ se tornaria ‘E’, e assim por diante. 
Implemente um  programa  que faça uso  desse Código de César, 
entre com uma string e retorne a string codificada. Exemplo:
String: a ligeira raposa marrom saltou sobre o cachorro cansado
Nova   string:   D   OLJHLUD   UDSRVD   PDUURP   VDOWRX   VREUH   R   FDFKRUUR FDQVDGR'''

import string
def listAlfabeto():
    alfabeto = string.ascii_lowercase
    texto = input('Digite um texto: ')
    novaLetra = ''
    step = 29
    inicial = 0
    for letra in texto:
        LetraAlfabeto = alfabeto.find(letra)
        if(LetraAlfabeto == -1):
            novaLetra += ' '
        else:
            y = LetraAlfabeto
            for x in range(0,step):
                y += 1
                if y > 26 -1:
                    y = 0
            LetraAlfabeto = y
            novaLetra += alfabeto[LetraAlfabeto]
            inicial += 1
    print(novaLetra)
listAlfabeto()
