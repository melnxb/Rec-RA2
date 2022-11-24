#ex.3  CALCULAR AREA

def calculo1(raio):
    valorPi= 3,14
    return valorPi * (raio**2)
    

def calculo2(lado):
    return lado**2


def calculo3(base, altura):
    return base*altura

continuaR=0
while True:

     print('Bem-vindo, escolha a forma geometrica que voce deseja calcular a area(em centimetros): \n 1.circulo\n 2. quadrado\n 3. restangulo')
     resposta = int(input('resposta:'))

     if resposta == 1:
        raio = float(input('Infrome o valor do raio: '))
        calCirculo = calculo1(raio)
        print(calCirculo)

     elif resposta ==2:
        lado = float(input('informe o valor do lado: '))
        calQuad = calculo2(lado)
        print(calQuad)
    
     elif resposta ==3:
        base = float(input('informe o valor do base: '))
        altura = float(input('informe o valor do altura: '))
        calRetang = calculo3(base,altura)
        print(calRetang)

     continuaR = int(input('1. Continuar?\n 2.Sair?: '))
     if continuaR==1:
        True
     else: 
        break


