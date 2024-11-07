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
ou 
import numpy as np
def notas():
    alunos_notas=np.array([],[])
    print("Digite o nome dos alunos:")
    for i in range (5):
        nome=input()
        alunos_notas=np.append(alunos_notas,nome)

    print("Digite as notas do alunos")
    for i in range (4):
        notas=float(input(f"Digite as notas do aluno {nome[i]}"))
        alunos_notas=np.append(alunos_notas,notas)

    print(alunos_notas)

notas()
