Player1=input()
Player2=input()
if(Player1=="rock"and Player2=="scissor"):
    print("Player1 win")
elif(Player1=="rock"and Player2=="paper"):
    print("Player1 win")
elif(Player1=="paper"and Player2=="scissor"):
    print("Player1 win")
elif(Player1 == Player2):
    print("replay")
else:
    print("Player2 win")