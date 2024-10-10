numeros = input("Digite vários números: ").split()


numerosInt = [int(numero) for numero in numeros]


print(sum(numerosInt))
