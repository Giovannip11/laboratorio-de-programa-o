1)

matriz=np.random.randint(1,11,size=(3,3))
print(matriz)

def determinante(matriz):
    determinante = np.linalg.det(matriz)
    return determinante !=0

if determinante(matriz):
    inversa=np.linalg.inv(matriz)
    print(inversa)
else:
    print("Não é possível fazer a inversa dessa matriz!")
2)
import numpy as np

matriz = np.random.randint(1,21,size=(4,4))
print(matriz)

def determinante():
    determinante=np.linalg.det(matriz)
    print(determinante)

def singular():
    if determinante==0:
        print("Matriz singular")
    else:
        print("Matriz não é singular")

determinante()
singular()
3)
import numpy as np

matriz = np.random.randint(1,16,size=(5,3))

print(matriz)

def transposta():
    matriz_transposta=np.transpose(matriz)
    print(matriz_transposta)
    print(matriz_transposta.shape)


print(matriz.shape)


transposta()
4)
import numpy as np

matriz= np.random.randint(1,101,size=(6,6))
print(matriz)

def média():
    media=np.mean(matriz)
    print(media)

def desvio_padrao():
    ds=np.std(matriz)
    print(ds)
def max():
    max=np.max(matriz)
    print(max)
def min():
    min=np.min(matriz)
    print(min)

média()
desvio_padrao()
max()
min()
