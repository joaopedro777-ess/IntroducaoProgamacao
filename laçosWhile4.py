njogadores=(int(input("Digite o número de jogadores: ")))
somaaltura=0
contador=0
while contador < njogadores:
    altura= float(input("digite a altura do jogador (contador+1):"))
    somaaltura+=altura
    contador+=1
alturamedia= somaaltura / njogadores
print("A altura média do time é", alturamedia,"metros.")