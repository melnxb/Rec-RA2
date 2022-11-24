#ex.4    falta organizar matriz soma..
matriz=[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def criamatriz(linhas,colunas):
    matriz=[]

    for i in range(linhas):
        listlinhas=[]
        for j in range(colunas):
            listlinhas.append(0)
    return matriz

####

for i in range(3):
    for j in range(3):
        matriz[i][j]= int(input('Informe os valores para a matriz: '))

#for linha in matriz:
print('-' * 30)
for linha in range(3):
    print(matriz[linha])
print('-' * 30)

valores=[]

for i in range(3):
    for j in range(3):
        if i==j:
            valores.append(matriz[i][j])

print(f'Valores da diagonal principal:\n{valores}\n')

soma= sum(valores)
maiorValor= max(valores)
menorValor= min(valores)

print(f'A soma dos valores d adiagonal principal é igual a: {soma}')
print(f'O maior valor é igual a: {maiorValor}')
print(f'O menor valor é igual a: {menorValor}')
