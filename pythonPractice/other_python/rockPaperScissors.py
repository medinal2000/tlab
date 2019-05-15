import getpass

#function to decide who is the winner
def winner(player1, player2):
    if player1.upper() == "R" and player2.upper() == "S":
        print("Player 1 wins!")
        
    elif player1.upper() == "P" and player2.upper() == "R":
        print("Player 1 wins!")
        
    elif player1.upper() == "S" and player2.upper() == "P":
        print("Player 1 wins!")
        
    elif player2.upper() == "R" and player1.upper() == "S":
        print("Player 2 wins!")
        
    elif player2.upper() == "P" and player1.upper() == "R":
        print("Player 2 wins!")
        
    elif player2.upper() == "S" and player1.upper() == "P":
        print("Player 2 wins!")
        
    else:
        print("No winner.\n")


#play rock paper scissors
print("Let's play rock paper scissors! Enter R for rock, P for paper, S for scissors, and Q to stop")

player1 = str(input("Player 1: "))
player2 = str(input("Player 2: "))

winner(player1, player2);


#continue playing until one of the player quits

while player1.upper() != "Q" and player2.upper() != "Q":
    print("Enter R for rock, P for paper, S for scissors, and Q to stop")

    player1 = str(input("Player 1: "))
    player2 = str(input("Player 2: "))
    
    winner(player1, player2);
    
print("\nGAME OVER")
   
   
