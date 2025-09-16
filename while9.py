n=int(input("Digite um número:  "))
cont=0
d=1
while d<=n:
    if n%d==0:
        cont+=1
    d+=1
if cont==2:
    print ("o número é primo")
else:
    print("O número mão é primo")           