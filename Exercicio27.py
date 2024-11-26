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
def ler_matriz(nome):
    matriz=[]
    print("Digite os elementos da {nome} 3x3:")
    for i in range (3):
        linha=[]
        for j in range (3):
            elemento = int(input(f"Elemento [{i},{j}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return np.array(matriz)

matriz1=ler_matriz("Matriz1")
matriz2=ler_matriz("Matriz2")
def somaMatriz():
    soma=matriz1+matriz2
    print(soma)
def multiplicacao():
    multi=matriz1*matriz2
    print(multi)
def subtracao():
    sub=matriz1-matriz2
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

3)
import numpy as np
diaSemana=7
bairros=int(input("Digite o número de bairros: "))

consumo = np.random.randint(100,500,size=(diaSemana,bairros))

def consumo_medio(matriz):
    return np.mean(matriz,axis=0)

def maior_consumo(matriz):
   return np.argmax(np.sum(matriz,axis=1))

def menor_consumo(matriz):
    return np.argmin(np.sum(matriz,axis=1))
    
    
print(f"Consumo médio por bairro: {consumo_medio(consumo)}")
print(f"Dia da semana com maior consumo: {maior_consumo(consumo)}")
print(f"Dia da semana com menor consumo: {menor_consumo(consumo)}")
