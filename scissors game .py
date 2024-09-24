from getpass import getpass as input
player_score1 = 0
player_score2 = 0
print("!Rock, Papers, Scissors Game Of The Decade!")
print()
while player_score1 < 3 and player_score2 < 3:
# Player 1's turn
  player1_weapon = input("Player 1, enter your move (R, P, or S): ").upper()

# Player 2's turn (using getpass to hide their input)
  player2_weapon = input("Player 2, enter your move (R, P, or S): ").upper()

# Check if both inputs are valid


  if player1_weapon in ["R", "P", "S"] and player2_weapon in ["R", "P", "S"]:
# Compare Player 1's and Player 2's choices to determine the winner
    
    if player1_weapon == player2_weapon:
      print("It's a tie!")
    elif (player1_weapon == "R" and player2_weapon == "S") or \
         (player1_weapon == "P" and player2_weapon == "R") or \
         (player1_weapon == "S" and player2_weapon == "P"):
      print("Player 1 wins!")
      player_score1 += 1
    else:
      player_score2 += 1
      print("Player 2 wins!")
  else:
    print("Invalid choice from one or both players. Please pick R, P, or S.")
    continue
if player_score1 == 3:
  print("Player 1 wins the game!")
else:
  print("Player 2 wins the game!")
  exit()
