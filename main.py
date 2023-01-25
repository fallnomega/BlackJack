import random

from art import logo

def init_cards():
    initial_cards = []
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for x in range(2):
        initial_cards.append(random.choice(cards))
    return initial_cards


def deal_card(hand):
    """Returns a random card from the deck."""

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand.append(random.choice(cards))
    return hand

def calculate_score(hand,user):
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
play= input("Do you want to play a game of Black Jack? Type 'y' or 'n': ")
keep_playing = False
if play == 'y':
    keep_playing = True
    # testing_hand = [11,10,10]
    # keep_playing = blackjack(testing_hand,'TESTING')
    player_cards = init_cards()
    print(f"Your cards: {player_cards} and Computer's first card: {player_cards[0]}")
    computer_cards = init_cards()
    player_score = calculate_score(player_cards,'Player')
    computer_score = calculate_score(computer_cards,"Dealer")
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
            player_score = calculate_score(player_cards, 'Player')
            keep_playing = blackjack(player_cards, 'Player')
            if computer_score < 17:
                computer_cards = deal_card(computer_cards)
                computer_score = calculate_score(computer_cards,'Computer')
                keep_playing = blackjack(computer_cards,'Computer')

        elif hit =='n':
            if computer_score < 17:
                computer_cards = deal_card(computer_cards)
                computer_score = calculate_score(computer_cards,'Computer')
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





