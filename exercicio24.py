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
2)
def soma_escalar():
  vetor1=[]
  vetor2=[]
  print("Digite os valores do vetor 1")
  for i in range(5):
      numero=int(input())
      vetor1.append(numero)
  print("Digite os valores do vetor 2")
  for i in range(5):
      numero = int(input())
      vetor2.append(numero)

  for i in range(5):
      soma=vetor1[i]+vetor2[i]
      i+=1
      print(soma)


soma_escalar()
3)
def soma_escalar():
  vetor1=[]
  vetor2=[]
  print("Digite os valores do vetor 1:")
  for i in range(5):
      numero=int(input())
      vetor1.append(numero)
  print("Digite os valores do vetor 2:")
  for i in range(5):
      numero = int(input())
      vetor2.append(numero)

  somaTotal = 0

  for i in range(5):
      somaTotal += vetor1[i]*vetor2[i]

  print(somaTotal)




soma_escalar()
4)
def maior_menor():
    vetor=[]
    print("Digite 15 números")

    for i in range(15):
        numero=int(input())
        vetor.append(numero)

    maior = vetor[0]
    menor = vetor[0]

    for numero in vetor:
        if numero > maior:
           maior = numero

        if numero < menor:
            menor = numero

    print("maior é:",maior)
    print("menor é:",menor)


maior_menor()
