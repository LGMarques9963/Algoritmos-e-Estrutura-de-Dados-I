from Pilha import Pilha
r = 1
jogador_1 = Pilha()
jogador_2 = Pilha()

jogador_1.push(1)
jogador_1.push(3)
jogador_1.push(6)
jogador_1.push(2)
jogador_1.push(9)

jogador_2.push(10)
jogador_2.push(7)
jogador_2.push(4)
jogador_2.push(8)
jogador_2.push(5)

def joga(p1,p2):
    print(f"Player 1's deck: {p1}")
    print(f"Player 2's deck: {p2}")

    carta_1 = p1.pop()
    carta_2 = p2.pop()

    print(f"Player 1 plays: {carta_1}")
    print(f"Player 2 plays: {carta_2}")


    if carta_1 > carta_2:
        print("Player 1 wins the round!")
        p1.push(carta_1)
        p1.push(carta_2)
    elif carta_2 > carta_1:
        print("Player 2 wins the round!")
        p2.push(carta_2)
        p2.push(carta_1)

while True:
    #print(f"Player 1's deck: {jogador_1}")
    #print(f"Player 2's deck: {jogador_2}")
    print(f"Round {r}")
    
    carta_1 = jogador_1.pop()
    carta_2 = jogador_2.pop()

    #print(f"Player 1 plays: {carta_1}")
    #print(f"Player 2 plays: {carta_2}")


    if carta_1 > carta_2:
        #print("Player 1 wins the round!")
        jogador_1.push(carta_1)
        jogador_1.push(carta_2)
    elif carta_2 > carta_1:
        #print("Player 2 wins the round!")
        jogador_2.push(carta_2)
        jogador_2.push(carta_1)
    

    r+=1
    if(jogador_1.isempty() or jogador_2.isempty()):
        break
    
    if r >=30:
        break
print(f"Player 1's deck: {jogador_1}")
print(f"Player 2's deck: {jogador_2}")
