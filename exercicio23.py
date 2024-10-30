1)
entrada = input("Digite uma sequência de números separados por espaço: ")


lista = list(map(int,entrada.split()))

print(sum(lista))
2)
n = input("Digite uma sequência de números separados por espaço: ")


lista= list(n)
lista = list(map(int,n.split()))
print(n)
for i in lista:
    if i % 2 == 0:
        print(i)

3)
n = input("Digite uma sequência de números separados por espaço: ")


lista= list(n)
lista = list(map(int,n.split()))
print("O menor número é:",min(lista))

print("O maior número é:",max(lista))
4)
n = input("Digite uma sequência de números separados por espaço: ")


lista= list(n)
lista = list(map(int,n.split()))
n = list(set(lista))
print(n)
5)Terminar em casa
n = input("Digite uma sequência de números separados por espaço: ")


lista= list(n)
num = 0
for i in lista:
    contagem = lista.count([num])
    num+=1
    print(contagem)
6)
n = input("Digite uma sequência de números separados por espaço: ")


lista= list(n)
lista = list(map(int,n.split()))
lista.reverse()
print(lista)
7)
n = input("Digite uma sequência de números separados por espaço: ")


lista= list(n)
lista = list(map(int,n.split()))
resultado = 1

for i in lista:
    resultado*=i

print(resultado)


