# -*- coding: utf-8 -*-
"""
@author: Venkatesh
"""

import random

DEFAULT_BANK_ROLL = 100

def deal_card():
    return random.randint(0, 12)

def get_card_name(number):
    """Get card name"""
    card_names = (
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    )
    return card_names[number]

def display_bankroll(bank_roll):
    """Print current bankroll"""
    print("You now have %s$" % bank_roll)

def check_outcome(dealer, n):
    outcome = "loss"
    if (n >= dealer[0]) and (n <= dealer[1]):
        outcome = "win"
    return outcome

def get_round_bet():
    print("Enter an option from below -\n")
    print("- Enter bet amount to play round")
    print("- Enter n to skip round")
    print("- Enter e or nothing to stop the game")
    return input("Enter your choice - \n")

def start_game():
    BANK_ROLL = DEFAULT_BANK_ROLL
    ROUND = 0
    while BANK_ROLL>0:
        ROUND += 1
        print("Round %s------------\n" % ROUND)
        dealer = [deal_card(), deal_card()]
        dealer.sort()
        print("Table - %s" % [get_card_name(x) for x in dealer])
        display_bankroll(BANK_ROLL)
        # ROUND_BET = int(input("Enter bet amount for this round (n to not bet this round)- "))
        ROUND_BET = get_round_bet()
        if ROUND_BET.lower() == 'n':
            print("Player decides to skip round.\n")
            continue
        elif ROUND_BET.lower() in ['e', '']:
            break
        ROUND_BET = int(ROUND_BET)
        if ROUND_BET>BANK_ROLL:
            ROUND_BET = int(input("You have bet more than your current bankroll. Please enter a valid value - "))
        print("Player Bets - %s$." % ROUND_BET)
        third_wheel = deal_card()
        print("Table - %s" % [get_card_name(x) for x in dealer])
        print("Third wheel is %s." % get_card_name(third_wheel))
        round_outcome = check_outcome(dealer=dealer, n=third_wheel)
        if round_outcome == "win":
            print("Player wins.\n")
            BANK_ROLL += ROUND_BET
        else:
            print("Player loses.\n")
            BANK_ROLL -= ROUND_BET
    if BANK_ROLL == 0:
        print("Bank roll is 0. Please recharge your account.")
    elif ROUND_BET.lower() in ['e', '']:
        print("Player has exited the game.")

if __name__=="__main__":
    start_game()
