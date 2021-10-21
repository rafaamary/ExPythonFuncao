'''Faça uma função que recebe por parâmetro o raio de 
uma esfera e calcula o seu volume v = 4/3xPI x R³, com PI = 3,14'''

def volume():
    raio = float(input('Digite o valor do Raio: '))
    print(((4/3)*3.14) * (raio**3))
volume()

  
