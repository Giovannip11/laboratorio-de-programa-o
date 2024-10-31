1)
def vetor_soma():
    vetor=[]

    print("Digite 10 números: ")
    for i in range (10):
        numero=int(input())
        vetor.append(numero)
        soma=sum(vetor)
        print(soma)

vetor_soma()
