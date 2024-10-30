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
5) 
n = input("Digite uma sequência de elementos separados por espaço: ")

lista = n.split()  
num_ocorrencias = {}


for num in lista:
    if num in num_ocorrencias:
        num_ocorrencias[num] += 1
    else:
        num_ocorrencias[num] = 1


print(num_ocorrencias)

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


