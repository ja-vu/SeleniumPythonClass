"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
 and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

user1 = input("Hi! What's your name? ")
user2 = input("Hey second player, what about you? What's your name? ")

print("ROCK - PAPER - SCISSOR \n")
u1_answer = input("%s, what will you play? " % user1)
u2_answer = input("%s, it's your turn. What do you choose? " % user2)


def compare(u1, u2):
    if u1 == u2:
        return("DRAW")

    elif u1 == 'rock':
        if u2 == 'scissor':
            return("Rock beats scissor. %s wins!" %user1)
        else:
            return("Paper beats rock. %s wins!" %user2)

    elif u1 =='scissor':
        if u2 == 'paper':
            return ("Scissor beats paper. %s wins!" %user1)
        else:
            return ("Rock beats scissor. %s wins!" %user2)

    elif u1 =='paper':
        if u2 == 'rock':
            return("Paper beats rock %s wins!" %user1)
        else:
            return("Scissor beats paper. %s wins!" %user2)

    else:
        return("Invalid input! You need to enter either rock, paper or scissor! Please try again.")


print(compare(u1_answer,u2_answer))
