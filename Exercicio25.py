1)
def vetor_impar():
    vetor=[]
    soma=0
    print("Digite 6 números inteiros")

    for i in range (6):
        numero=int(input())
        vetor.append(numero)

        if numero % 2 !=0:
            soma+=numero
    
    print(soma)
    vetor[4]=100
    vetor.pop()
    print(vetor)
    

vetor_impar()
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
6)
def pares():
    vetor=[]*10
    count=0
    par=[]
    print("Digite 10 valores inteiros:\n")
    for i in range (10):
        n=int(input())
        vetor.append(n)
        if n % 2 ==0:
            par.append(n)

            count+=1
    print("A quantidade de números pares é:",count)
    print("Os números pares são: ",par)
pares()
7)
def maior_menor():
    vetor=[]*10
    print("Digite 10 números inteiros:\n")
    for i in range (10):
        n=int(input())
        vetor.append(n)

    print("O maior é:",max(vetor))
    print("O menor é:",min(vetor))
maior_menor()
8)
def maior_posicao():
    vetor=[]*10
    print("Digite 10 números inteiros:\n")
    for i in range (10):
        n=int(input())
        vetor.append(n)
    maior=max(vetor)

    print("O maior é:",maior,"Sua posição é:",vetor.index(maior))

maior_posicao()
9)
def media():
    notas=[]*15
    print("Digite  a nota de 15 alunos:")
    for i in range (15):
        n=(int(input()))
        notas.append(n)

    soma=sum(notas)
    mediaGeral=soma/15
    print("A media geral foi:",mediaGeral)

media()
10)
def positivos_negativos():
    vetor=[]*10
    positivos=[]
    count=0
    print("Digite números reais:\n")
    for i in range(10):
        n=float(input())
        vetor.append(n)
        if n <0:
            count+=1
        if n >0:
            positivos.append(n)
    soma=sum(positivos)
    print(soma)
    print(count)
positivos_negativos()
11)
def posicao_maior_menor():
    vetor=[]*5
    print("Digite 5 valores inteiros:\n")
    for i in range (5):
        n=int(input())
        vetor.append(n)
    maior=max(vetor)
    menor=min(vetor)
    print("O maior está na ",vetor.index(maior)," posição")
    print("O menor está na ",vetor.index(menor)," posição")

posicao_maior_menor()
12)def valores_iguais():
        vetor = []*10
        print("Digite 10 números inteiros:")
        for i in range(10):
            n = int(input(f"Número {i + 1}: "))
            vetor.append(n)
    
   
        duplicados = set([x for x in vetor if vetor.count(x) > 1])
    
    
        if duplicados:
             print("Valores duplicados:", list(duplicados))
        else:
             print("Não há valores duplicados.")

valores_iguais()

13)
def valores_iguais():
    vetor=[]*20
    print("Digite 20 números inteiros:\n")
    for i in range (20):
        n=int(input())
        vetor.append(n)
    
    vetor_unicos=list(set(vetor))
    print(vetor_unicos)

valores_iguais()
14)
def processa_vetor():
    vetor=[]*5
    print("Digite números reais:\n")
    for i in range (5):
        n=float(input())
        vetor.append(n)
    escolha=int(input("Digite o que deseja fazer, 0 para sair, 1 mostrar vetor na ordem direta, 2 mostrar vetor na ordem inversa"))
    if escolha==0:
        print("FIM")
    elif escolha==1:
        print("Vetor na ordem direta:",vetor)
    elif escolha==2:
        vetor.reverse()
        print("Vetor na ordem inversa:",vetor)
    else:
        print("Código inválido")
processa_vetor()


