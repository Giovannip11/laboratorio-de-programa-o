1)
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
