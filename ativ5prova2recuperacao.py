#João pedro, Márcio, Kauã
num=int(input("Digite um número:"))
palin=0
normal=num
while normal>0:
    digito=normal%10
    palin=palin*10+digito
    normal=normal//10
print("Número ao contário", palin)
if num==palin:
    print("o número é um palíndromo ")
else:

    print("O número não é um palindromo") 
