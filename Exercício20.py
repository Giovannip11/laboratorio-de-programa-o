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
