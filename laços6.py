#Fa¸ca um programa que receba as notas (n1,n2,n3) de 10 alunos e calcule a m´edia de cada aluno,
#mostre a maior e a menor m´edia. Assumindo que a m´edia ´e 6, mostre a quantidade de alunos
#aprovados e reprovados.
maior=0
menor=10
ap=0
rep=0
for i in range(10):
    n1=float(input("n1"))
    n2=float(input("n2"))
    n3=float(input("n3"))
    media=(n1+n2+n3)/3
    if media>=6:
        ap+=1
    else:
        rep+=1
    if media>maior:
        maior=media
    elif media<menor:
        menor=media
print(maior,menor,ap,rep)