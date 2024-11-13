1)
import numpy as np

def lerMatriz():
    count=0
    matriz=np.random.randint(0,11,size=(5,5))
    print(matriz)
    for i in matriz:
        for j in i:
            if j != 0:
                count += 1
    print(count)

lerMatriz()
2)
import numpy as np
matriz1=np.random.randint(0,11,size=(3,3))
matriz2=np.random.randint(0,11,size=(3,3))
def somaMatriz():
    soma=matriz1+matriz2
    print(soma)
def multiplicacao():
    multi=matriz1*matriz2
    print(multi)
def subtracao():
    sub=matriz1=matriz2
    print(sub)
opcao=int(input("Digite a opção que deseja:\n1)Imprimir matrizes.\n2)Calcule e imprima a soma de todos os elementos das matrizes.\n3)Calcule e imprima  a multiplicação dos elementos das matrizes.\n4)Calcule e imprima a subtração dos elementos das matrizes.\n"))

if opcao==1:
    print("Matriz1:\n", matriz1)
    print("Matriz2:\n", matriz2)
if opcao==2:
    somaMatriz()
elif opcao==3:
    multiplicacao()
elif opcao==4:
    subtracao()
