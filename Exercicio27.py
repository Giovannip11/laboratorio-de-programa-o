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
