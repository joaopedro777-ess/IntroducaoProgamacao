
maior_media = 0
menor_media = 99999
qtdeap=0
qtderep=0
aluno=0
i=0

while  aluno<=10:
    n1 = float(input("Digite a primeira nota do aluno : "))
    n2 = float(input("Digite a segunda nota do aluno : "))
    n3 = float(input("Digite a terceira nota do aluno : "))
    media = (n1 + n2 + n3) / 3
    aluno = i + 1
    print("A média do aluno", aluno, "é:", media)
    if media >= 6:
        print("Aluno aprovado")
        aprovados = aprovados + 1
    else:
        print("Aluno reprovado")
        reprovados = reprovados + 1
    if maior_media is 0 or media > maior_media:
        maior_media = media
    if menor_media is 99999 or media < menor_media:
        menor_media = media
print("Número de alunos aprovados:", aprovados)
print("Número de alunos reprovados:", reprovados)
print("Maior média:", maior_media)
print("Menor média:", menor_media)