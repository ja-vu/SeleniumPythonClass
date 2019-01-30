"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

a = 0
while a != -1:

    print("ROCK-PAPER-SCISSOR")
    player1 = input("PLAYER 1 STARTS: ")
    player2 = input("PLAYER 2'S TURN: ")

    if player1 == player2:
        print("DRAW")

    # ROCK vs PAPER
    if player1 == 'paper' and player2 == "rock":
        print("PAPER BEATS ROCK! PLAYER 1 WINS")
    if player1 == 'rock' and player2 == "paper":
        print("PAPER BEATS ROCK! PLAYER 2 WINS")

    # ROCK vs SCISSOR
    if player1 == 'rock' and player2 == "scissor":
        print("ROCK BEATS SCISSOR! PLAYER 1 WINS")
    if player1 == 'scissor' and player2 == "rock":
        print("ROCK BEATS SCISSOR! PLAYER 2 WINS")

    # SCISSOR vs PAPER
    if player1 == 'scissor' and player2 == "paper":
        print("SCISSOR BEATS PAPER! PLAYER 1 WINS")
    if player1 == 'paper' and player2 == "scissor":
        print("SCISSOR BEATS PAPER! PLAYER 2 WINS")

    print()
    print("====== NEW ROUND =====")
