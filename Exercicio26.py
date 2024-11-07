1)
import numpy as np
def notas():
    notas=np.array([], dtype=float)
    alunos=np.array([], dtype=str)
    print("Digite os nome do aluno:")
    for i in range (5):
        nome=(input())
        alunos=np.append(alunos,nome)
    print("Digite as suas notas:")
    for i in range (4):
        n=float(input(f"Digite a nota do aluno {alunos[i]}"))
        notas=np.append(notas,n)

    notas_alunos = np.array(alunos, notas)
    print(notas_alunos)

notas()
