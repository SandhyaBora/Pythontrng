def rockpaperscissor (player1,player2):
    if(player1 == player2):
       return player,player2
    elif(player1=="scissor" and player2=="rock"):
        return player1
    elif(player1=="scissor" and player2=="paper"):
        return player1
    elif(player1=="paper" and player2=="rock"):
        return player1
    else:
        return player2
s=rockpaperscissor("paper","scissor")
print("win")