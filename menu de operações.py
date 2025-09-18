import os
print("**********OPERAÇÕES MATEMÁTICAS**********")
print("escolha uma das operações abaixo. Para encerrar digite sair!!!!!!!! ")
print("1- Soma ")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")
print("5- Par ou impar")
print("6- Primo")
print("7- Fatorial")
opcao=input("Digite a opção desejada ou <SAIR> para encerrar")
opcaoMaiusc=opcao.lower()
while opcaoMaiusc != "sair":
    if opcao=="1":
        n1=int(input("Digite o primeiro número: "))
        n2=int(input("Digite o segundo número número:"))
        print("O resultado da soma entre o número", n1, "e o número", n2, "é", n1+n2,".")
    if opcao=="2":
        n1=int(input("Digite o primeiro número: "))
        n2=int(input("Digite o segundo número número:"))
        print("O resultado da subtração entre o número", n1, "e o número", n2, "é", n1-n2,".")
    if opcao=="3":
        n1=int(input("Digite o primeiro número: "))
        n2=int(input("Digite o segundo número número:"))
        print("O resultado do produto entre o número", n1, "e o número", n2, "é", n1*n2,".")
    if opcao=="4":
        n1=int(input("Digite o primeiro número: "))
        n2=int(input("Digite o segundo número número:"))
        print("O resultado da divisão entre o número", n1, "e o número", n2, "é", n1/n2,".")
    if opcao=="5":
        n1=int(input("Digite o número para saber se ele é impar ou par"))
        if n1%2==0:
            print("O número", n1, "é par")
        else:
            print("O número", n1, "é impar")
input("Pressione ENTER para voltar ao MENU!")
os.system ("cls")
