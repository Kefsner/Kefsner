import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

should_start = False

lets_play = input("Do you want to play a game of Blackjack? Type 'y' for yes or 'n' for no: ").lower()

if lets_play == "y":
    should_start = True
    print(logo)

while should_start:
    user_hand = []
    computer_hand = []

    for n in range(2):
        user_hand.append(cards[random.randint(0, len(cards) - 1)])
    computer_hand.append(cards[random.randint(0, len(cards) - 1)])
    current_score = sum(user_hand)

    get_card = True

    while current_score <= 21 and get_card:
        print(f"Your cards: {user_hand}, current score: {current_score}")
        if current_score == 21:
            print("Blackjack!")
        print(f"Computer's first card: {computer_hand[0]}")
        draw_card = input("Type 'y' to get another card or type 'n' to pass: ")
        if draw_card == "y":
            user_hand.append(cards[random.randint(0, len(cards) - 1)])
            current_score = sum(user_hand)
            if current_score > 21 and 11 in user_hand:
                user_hand[user_hand.index(11)] = 1
                current_score = sum(user_hand)
        else:
            get_card = False

    computer_score = sum(computer_hand)

    while computer_score < 17:
        computer_hand.append(cards[random.randint(0, len(cards) - 1)])
        computer_score = sum(computer_hand)

    while computer_score <= current_score:
        computer_hand.append(cards[random.randint(0, len(cards) - 1)])
        computer_score = sum(computer_hand)
        if computer_score > 21 and 11 in computer_hand:
            computer_hand[computer_hand.index(11)] = 1
            computer_score = sum(computer_hand)
    if current_score > 21:
        print(f"Your final hand: {user_hand}, current score: {current_score}")
        print("You went over. You lose...")
    elif computer_score > 21:
        print(f"Your final hand: {user_hand}, current score: {current_score}")
        if current_score == 21:
            print("Blackjack!")
        print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
        print("Opponent went over. You win!")
    elif current_score > computer_score:
        print(f"Your final hand: {user_hand}, current score: {current_score}")
        if current_score == 21:
            print("Blackjack!")
        print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
        print("You win!")
    elif current_score < computer_score:
        print(f"Your final hand: {user_hand}, current score: {current_score}")
        print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
        print("You lose...")
    again = input("Want to play again? Type 'y' or 'n'.: ").lower()

    if again == "n":
        should_start = False
