1)def calcular_media():
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    media=(nota1+nota2+nota3)/3
    return media

media=calcular_media()
if media>=7:
    print("Aluno aprovado")
elif media<7 and media>5:
    print("Recuperação")

else:
    print("Reprovado")

2)def celsius_para_farenheint():
    celsius= float(input("Digite a temperatura em celsius: "))
    F=celsius*1.8+32
    return F

def farenheint_para_celsius():
    fahrenheit=float(input("Digite a temperatura em fahrenheit: "))
    C = (fahrenheit-32) * (5/9)
    return C

escolha = int(input("Digite o que deseja converter 1 para celsius para farenheint, 2 para farenheint para celsius:"))
if escolha == 1:
    resultado=celsius_para_farenheint()
    print("A temperatura em farenheint é:",resultado)
elif escolha ==2:
    resultado=farenheint_para_celsius()
    print("A temperatura em celsius é:",resultado)

3)
def eh_primo(numero):
    
    if numero < 2:
        return False

    
    for i in range(2, numero):
        if numero % i == 0:
            return False  
    
    return True 


numero = int(input("Digite um número inteiro que deseja saber se é primo: "))


if eh_primo(numero):
    print(f"O número é primo.")
else:
    print(f"O número não é primo.")

4)
def gerar_tabuada(numero):
    
    for i in range(1, 11):
        resultado = numero * i
        print(resultado)


numero = int(input("Digite um número: "))
gerar_tabuada(numero)
5)
def contar_vogais(texto):
    vogais = "aeiouAEIOU" 
    contador = 0 
    
   
    for char in texto:
        if char in vogais:
            contador += 1  
    
    return contador  


texto = input("Digite uma palavra ou frase: ")


total_vogais = contar_vogais(texto)
print(total_vogais)
