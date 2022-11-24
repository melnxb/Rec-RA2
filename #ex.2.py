#ex.2
listaImpar=[]
listaPar=[]
listaV =[0,0,0,0,0,0,0,0,0,0]


def listPar(lista):

    for par in listaV:
         if par %2 == 0:
            listaPar.append(par)
    return listaPar


def listImpar(lista):

    for impar in listaV:
        if impar %2 != 0:
             listaImpar.append(impar)
    return listaImpar

    
#############              cod PRINCIPAL                          ############

for i in range(10):
     listaV[i] = int(input('Digite um valor inteiro: '))

print(listaV)

listaPar=listPar(listaV)
print(f'PARES:\n{listaPar}')

listaImpar=listImpar(listaV)
print(f'IMPAR:\n{listaImpar}')

