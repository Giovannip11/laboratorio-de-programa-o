1)
numeros = input("Digite vários números: ").split()


numerosInt = [int(numero) for numero in numeros]


print(sum(numerosInt))
2)

valores = input("Digite valores booleanos (True ou False): ").split()


boolean = [valor == 'True' for valor in valores]

print(bool(boolean))


if all(boolean):
    print("Tudo na lista é True")
else:
    print("Nem todos os valores na lista são True")

3)
#Não consegui
valor = list(input("Digite valores:").split())

if valor =="True":
    valorBool = [valor == 'True' for valor in valor]
    print(type(valorBool))

4)
frase=input("Digite uma frase:")
print(len(frase))
5)
numeros = input("Digite vários números: ").split()


numerosInt = [int(numero) for numero in numeros]

print(max(numerosInt))
6)
numeros = input("Digite vários números: ").split()


numerosInt = [int(numero) for numero in numeros]

print(min(numerosInt))
7)
numeroNegativo = int(input("Digite um número negativo:"))
if numeroNegativo>0:
    print("ERRO")
else:
    print(abs(numeroNegativo))
8)
numeros=input("Digite uma serie de numeros: ").split()

numerosInt = [int(numero) for numero in numeros]

print(sorted(numerosInt))
9)
for i in range (11):
    print(i)

10)
frase= input("Digite uma frase:")

inversao = ''.join(reversed(frase))

print(inversao)
11)
valores = input("Digite valores booleanos (True ou False): ").split()


boolean = [valor == 'True' for valor in valores]

print(bool(boolean))


if all(boolean):
    print("Tudo na lista é True")
else:
    print("Nem todos os valores na lista são True")

