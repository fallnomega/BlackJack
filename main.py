import random

from art import logo

def init_cards():
    initial_cards = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for x in range(2):
        initial_cards.append(random.choice(cards))
    # print (initial_cards)

    return initial_cards


def deal_card(hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand.append(random.choice(cards))
    return hand

def score (hand,user):
    score = 0
    for x in hand:
        score+=x
    return score

def blackjack(hand,user):
    score = 0
    for x in hand:
        score+=x
    if int(score) == 21:
        print(f"{user} with a hand of {hand} has a Black Jack, WE HAVE A WINNER!")
        exit()
    elif int(score) > 21:
        for x in hand:
            if x == 11 and (score - 10) > 21:
                print(f"{user}'s score is {score} which is above 21 even with adjusting the Ace to 1. {user} loses the game!")
                exit()
            elif x == 11 and (score - 10) == 21:
                print(f"{user} with a hand of {hand} has a Black Jack due to Ace being a 1 in this case thus making the score {score-10}, WE HAVE A WINNER!")
                exit()

        print(f"{user} with a {hand} totaling {score} loses the game")
        exit()

    else:
        return True





print(logo)
print("Do you want to play a game of Black Jack? Type 'y' or 'n': ")
play = 'y'
# play= input("Do you want to play a game of Black Jack? Type 'y' or 'n': ")
keep_playing = False
if play == 'y':
    keep_playing = True
    # testing_hand = [11,10,10]
    # keep_playing = blackjack(testing_hand,'TESTING')
    player_cards = init_cards()
    print(f"Your cards: {player_cards} and Computer's first card: {player_cards[0]}")
    computer_cards = init_cards()
    player_score = score(player_cards,'Player')
    computer_score = score(computer_cards,"Dealer")
    keep_playing = blackjack(player_cards,'Player')
    keep_playing = blackjack(computer_cards,'Dealer')
    while keep_playing == True:
        print(f"Player's score = {player_score} and Dealer's score = {computer_score}")
        print(f"")
        hit = input("Deal another card? [y/n]").lower()
        if hit != 'y' and hit !='n':
            print("Wrong selection, exitting program")
            exit()
        elif hit =='y':
            player_cards = deal_card(player_cards)
            player_score = score(player_cards, 'Player')
            keep_playing = blackjack(player_cards, 'Player')
            if computer_score < 17:
                computer_cards = deal_card(computer_cards)
                computer_score = score(computer_cards,'Computer')
                keep_playing = blackjack(computer_cards,'Computer')

        elif hit =='n':
            if computer_score < 17:
                computer_cards = deal_card(computer_cards)
                computer_score = score(computer_cards,'Computer')
                keep_playing = blackjack(computer_cards,'Computer')
            else:
                if computer_score > player_score:
                    print(f"Dealer has {computer_score} while Player has {player_score}. Dealer WINS!!!!")
                    keep_playing=False
                elif player_score > computer_score:
                    print(f"Player has {player_score} while Dealer has {computer_score}. Player WINS!!!!")
                    keep_playing = False
                else:
                    print (f"Player has {player_score} while Dealer has {computer_score}. DRAW!!!!")
                    keep_playing = False

else:
    print ("Goodbye Player!")





############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.