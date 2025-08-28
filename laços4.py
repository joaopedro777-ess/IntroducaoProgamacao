#Escreva um programa que leia um valor correspondente ao n´umero de jogadores de um time
#de vˆolei. O programa dever´a ler uma altura para cada um dos jogadores e, ao final, informar
#a altura m´edia do time
n=int(input("num de jogadores"))
altura=0
for j in range(n):
    a=float(input("altura do jogador"))
    altura+=a
print(altura / n)
