
num_jogadores = int(input("Digite o número de jogadores do time: "))

soma_alturas = 0
contador = 0

while contador < num_jogadores:
    altura = float(input("Digite a altura do jogador (contador + 1): "))
    soma_alturas += altura
    contador += 1
altura_media = soma_alturas / num_jogadores
print("A altura média do time é: ",altura_media," metros.")
