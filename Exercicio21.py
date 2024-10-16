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
