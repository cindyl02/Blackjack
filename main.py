from art import logo
import os
import random


def draw_card():
    """ Returns a random card from list of possible cards
    :return: random card
    """
    card_values = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(card_values)


def compare_scores(comp_score, user_score):
    """ Takes a computer score and user score and prints the final result of the game by comparing the two scores
    :param comp_score: computer score
    :param user_score: user score
    """
    if comp_score > 21 and user_score > 21:
        print("You went over. You lose.")
    elif user_score == comp_score:
        print("It's a draw.")
    elif comp_score == 0:
        print("Computer has a blackjack. You lose.")
    elif user_score == 0:
        print("Blackjack! You win.")
    elif user_score > 21:
        print("You went over. You lose.")
    elif comp_score > 21:
        print("Computer went over. You win.")
    elif user_score > comp_score:
        print("You win.")
    else:
        print("You lose.")


def calculate_score(cards):
    """ Take a list of cards and return 0 if there is a blackjack (ace + 10 = 21)
    Otherwise, if there is an ace and the sum is over 21, replace ace with value of 1

    :param cards: list of cards
    :return: sum of cards
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def play_game():
    print(logo)
    should_end = False
    user_hand = []
    comp_hand = []
    for _ in range(2):
        user_hand.append(draw_card())
        comp_hand.append(draw_card())
    while not should_end:
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(comp_hand)
        print(user_score, computer_score)
        print(f"Your cards: {user_hand}. Your score: {21 if user_score == 0 else user_score}. Computer's first card: {comp_hand[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            should_end = True
        else:
            draw_again = input('Do you want to draw another card? Type "yes" or "no": ')
            if draw_again == "yes":
                user_hand.append(draw_card())
            else:
                should_end = True
    while computer_score != 0 and computer_score <= 16:
        comp_hand.append(draw_card())
        computer_score = calculate_score(comp_hand)
    print(f"Your cards: {user_hand}. Your score: {21 if user_score == 0 else user_score}.")
    print(f"Computer cards: {comp_hand}. Computer score: {21 if computer_score == 0 else computer_score}.")
    compare_scores(computer_score, user_score)


if __name__ == '__main__':
    while input('Do you want to play a game of blackjack? Type "yes" or "no": ') == "yes":
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")
        play_game()
