2)
def ler_tamanho():
    a=int(input("Digite o tamanho do vetor: "))
    vetor =[]*a
    for i in range (a):
        numero=int(input())
        vetor.append(numero)

    print(vetor)

ler_tamanho()
3)
def vetor1_vetor2():
    n=int(input("Digite o tamanho do vetor: "))
    vetor1 =[]*n
    for i in range (n):
      numero=int(input())
      vetor1.append(numero)


    print(vetor1)
    vetor1.reverse()
    print(vetor1)


vetor1_vetor2()
4)
def quadrado():
    vetor=[]*10
    vetorQuadrado=[]*10
    print("Digite valores reais:\n")
    for i in range (10):
        n = float(input())
        vetor.append(n)
        n = n**2
        vetorQuadrado.append(n)
    print(vetor)
    print(vetorQuadrado)

quadrado()
5)
def ler_XY():
    vetor=[]*8
    print("Digite os valores do vetor:\n")
    for i in range (8):
        n=int(input())
        vetor.append(n)

    x=int(input("Digite um valor para X: "))
    y=int(input("Digite um valor para Y: "))
    soma=vetor[x]+vetor[y]
    print(soma)

ler_XY()
