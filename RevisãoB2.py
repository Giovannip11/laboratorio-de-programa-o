1)
import numpy as np

matriz=np.random.randint(1,101,size=(6,6))
print(matriz)

def media():
    media=np.mean(matriz)
    print(media)

def valorMax():
    valorMax=np.max(matriz)
    print(valorMax)

def valorMin():
    min=np.min(matriz)
    print(min)

def desvioPadrao():
    desvio=np.std(matriz)
    print(desvio)
media()
valorMax()
valorMin()
desvioPadrao()
2)
import numpy as np

coluna=3
linha=3
matriz1=[]
print("Digite os valores que vão entrar na matriz1: ")
for i in range(3):
    linha=[]
    for j in range(3):
        elemento=int(input(f"Elemento [{i},{j}] da matriz1: "))
        linha.append(elemento)
    matriz1.append(linha)

matriz1=np.array(matriz1)


matriz2=[]
print("Digite os valores que vão entrar na matriz2: ")
for i in range(3):
    linha=[]
    for j in range(3):
        elemento=int(input(f"Elemento [{i},{j} da matriz2]"))
        linha.append(elemento)
    matriz2.append(linha)

matriz2=np.array(matriz2)

def imprimirMatrizes():
    print(matriz1)
    print(matriz2)

def somaMatriz():
    soma=matriz1+matriz2
    print(soma)
def multiplicacao():
    mult=matriz1*matriz2
    print(mult)
def sub():
    sub=matriz1-matriz2
    print(sub)
escolha=int(input("Digite o que deseja fazer, 1-imprimir matrizes.2-soma das matrizes.3-Multiplicação das matrizes.4-subtração das matrizes:"))    
if escolha ==1:
   imprimirMatrizes()
if escolha==2:
    somaMatriz()
if escolha ==3:
    multiplicacao()
if escolha==4:
    sub()
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
4)
import numpy as np

dia=30
reservatorio=int(input("Digite o número de reservatorios: "))

matriz=np.random.randint(100,500,size=(dia,reservatorio))

def media_pureza(matriz):
    return np.mean(matriz,axis=0)
def melhor_pior(matriz):
    melhor_dia=np.argmax(np.max(matriz,axis=1))
    return melhor_dia
def pior_melhor(matriz):
    pior_dia=np.argmin(np.min(matriz,axis=1))
    return pior_dia
def reservatorio_maior_media_pureza(matriz):
    maior_media=np.argmax(np.mean(matriz,axis=0))
    return maior_media
def reservatorio_menor_media_pureza(matriz):
    menor_media=np.argmin(np.mean(matriz,axis=0))
    return menor_media


print(f"Média de pureza: {media_pureza(matriz)}")
print(f"Melhor dia é: {melhor_pior(matriz)}")
print(f"Pior dia é: {pior_melhor(matriz)}")
print(f"Maior media de pureza {reservatorio_maior_media_pureza(matriz)}")
print(f"Menor media de pureza {reservatorio_menor_media_pureza(matriz)}")

5)
import numpy as np

alunos = 3
notas = 4


matriz = np.zeros((alunos, notas))
nomes = []


print("Digite os nomes dos alunos: ")
for i in range(alunos):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nomes.append(nome)


print("\nDigite as notas dos alunos: ")
for i in range(alunos):
    for j in range(notas):
        matriz[i, j] = float(input(f"Digite a nota {j+1} do aluno {nomes[i]}: "))


print("\nMatriz de notas:")
for i in range(alunos):
    print(f"{nomes[i]}: {matriz[i]}")
