#Joao pedro, Márcio, Kauã

numero = input("Digite um número inteiro: ")

soma = 0
quantidade = 0

for digito in numero:
    d = int(digito)
    soma = soma + d
    quantidade += 1

media = soma / quantidade

mais_proximo = int(numero[0])
menor_diferenca = abs(int(numero[0]) - media)

for digito in numero:
    d = int(digito)
    diferenca = abs(d - media)
    if diferenca < menor_diferenca:
        menor_diferenca = diferenca
        mais_proximo = d

print("Média dos dígitos:", media)
print("Dígito mais próximo da média:", mais_proximo)
