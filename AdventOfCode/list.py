import numpy as np

jogador_1 = np.genfromtxt("player_1.txt",dtype="int",delimiter="\n")
jogador_2 = np.genfromtxt("player_2.txt",dtype="int",delimiter="\n")
jogador_1 = [int(i) for i in jogador_1]
jogador_2 = [int(i) for i in jogador_2]

while True:
    carta_1 = jogador_1.pop(0)
    carta_2 = jogador_2.pop(0)

    if carta_1 > carta_2:
        #print("Player 1 wins the round!")
        jogador_1.append(carta_1)
        jogador_1.append(carta_2)
    elif carta_2 > carta_1:
        #print("Player 2 wins the round!")
        jogador_2.append(carta_2)
        jogador_2.append(carta_1)

    if (len(jogador_1) == 0):
        vencedor = jogador_2
        break
    if(len(jogador_2) == 0):
        vencedor = jogador_1
        break

print(f"Player 1's deck: {jogador_1}")
print(f"Player 2's deck: {jogador_2}")

score = 0

for i in range(len(vencedor)):
    score+=vencedor[i] * (len(vencedor) - i)