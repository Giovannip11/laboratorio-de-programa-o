1)
import numpy as np

def notaAluno():
    num_alunos=3
    num_notas=4

    alunos_nota=np.zeros((num_alunos,num_notas))
    nomes=[]
    print("Digite o nome dos alunos:")
    for i in range (num_alunos):
        nome=input(f"Digite o nome dos alunos{i+1}: ")
        nomes.append(nome)
    print("\nDigite as notas dos alunos:")
    for i in range (num_alunos):
        for j in range(num_notas):
            nota=float(input(f"Digite a nota {j+1} do aluno {nomes[i]}:"))
            alunos_nota[i,j]=nota
    print("\nMatriz de notas:")
    for i in range (num_alunos):
        print(f"{nomes[i]}: {alunos_nota[i]}")

notaAluno()
2)
import numpy as np

def notaAluno():
    num_alunos=3
    num_notas=4

    alunos_nota=np.zeros((num_alunos,num_notas))
    nomes=[]
    print("Digite o nome dos alunos:")
    for i in range (num_alunos):
        nome=input(f"Digite a nota do aluno{i+1}: ")
        nomes.append(nome)
    print("\nDigite as notas dos alunos:")
    for i in range (num_alunos):
        for j in range(num_notas):
            nota=float(input(f"Digite a nota {j+1} do aluno {nomes[i]}:"))
            alunos_nota[i,j]=nota
    print("\nMatriz de notas:")
    for i in range (num_alunos):
        print(f"{nomes[i]}: {alunos_nota[i]}")
    segundaNotaDoPrimeiroAluno=alunos_nota[0,1]
    quartaNotaDoTerceiroAluno=alunos_nota[2,3]
    print(f"A segunda nota do aluno {nomes[0]} é {segundaNotaDoPrimeiroAluno}")
    print(f"A quarta nota do aluno {nomes[2]} é {quartaNotaDoTerceiroAluno}")

notaAluno()
3)
import numpy as np

def posicao():
    coluna=3
    linha=4
    tabela=np.zeros((coluna,linha))
    for i in range(linha):
        for j in range(coluna):
            tabela[j,i]=j*i
    print(tabela) 
    

posicao()
4)
import numpy as np
def umAdez():
    vetor1=np.linspace(1,10,10,dtype=int)
    print(vetor1)
    quadrado=vetor1**2
    print(quadrado)

umAdez()
5)
import numpy as np
def aleatorio():
    linha=3
    coluna=3
    matriz=np.random.randint(2,size=(linha,coluna))
    print(matriz)
    print(matriz.sum())



    
aleatorio()
6)
import numpy as np
def somaVetor():
    vetor1=np.random.randint(1,11,size=5)
    vetor2=np.random.randint(1,11,size=5)
    print(vetor1)
    print(vetor2)
    soma=vetor1+vetor2
    print(f"soma é igual a{soma}")
    produto=vetor1*vetor2
    print(f"produto é igual a {produto}")

somaVetor()
7)
import numpy as np
def aleatorios20():
    matriz=np.random.randint(21,size=(4,4))
    print(matriz)

    submatriz=matriz[1:3,1:3]
    print("*///////////////////")
    print(submatriz)

aleatorios20()
8)
import numpy as np
def produtoMatricial():
    tamanho=int(input("Digite a o tamanho da matriz: "))
    matriz1=np.zeros((tamanho,tamanho),dtype=int)
    matriz2=np.zeros((tamanho,tamanho),dtype=int)

    print("\nDigite os elementos da primeira matriz:")
    for i in range(tamanho):
        for j in range(tamanho):
            matriz1[i, j] = int(input(f"Elemento [{i+1},{j+1}]: "))
    
    print("\nDigite os elementos da segunda matriz:")
    for i in range(tamanho):
        for j in range(tamanho):
            matriz2[i, j] = int(input(f"Elemento [{i+1},{j+1}]: "))
    
        print("\nMatriz 1:")
    print(matriz1)
    print("\nMatriz 2:")
    print(matriz2)

    produto = np.dot(matriz1, matriz2)
    print("\nProduto Matricial:")
    print(produto)

produtoMatricial()


