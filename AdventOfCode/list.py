jogador_1 = [9,2,6,3,1]
jogador_2 = [5,8,4,7,10]

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

    if((len(jogador_1) == 0) or (len(jogador_2) == 0)):
        break

print(f"Player 1's deck: {jogador_1}")
print(f"Player 2's deck: {jogador_2}")