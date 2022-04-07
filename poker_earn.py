# -*- coding: utf-8 -*-
from InputError import IllegalHand


def card_value(card):
    """Returns the numeric value of a poker card."""
    return {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
        "7": 7, "8": 8, "9": 9, "10": 10, "J": 11,
        "Q": 12, "K": 13, "A": 14
        }[card.split("-")[0]]


def card_color(card):
    """Returns the color value of a poker card."""
    return card.split("-")[1]


def hand_value(hand):
    """Returns the numerical value of all poker cards in the hand."""
    return map(card_value, hand)


def hand_color(hand):
    """Returns the color value of all poker cards in the hand."""
    return map(card_color, hand)


def poker_score(hand):
    """Returns the hand score according to standard poker rules."""
    if not is_unique_element(hand):
        raise IllegalHand

    count = hand_count(hand)
    high = high_card(hand)
    is_straight = hand_is_straight(hand)
    is_flush = hand_is_flush(hand)

    if is_flush:
        if is_straight:
            if high == 14:
                return 9
            else:
                return 8
        else:
            return 5
    elif is_straight:
        return 4
    elif count[0] == 4:
        return 7
    elif count[0] == 3 and count[1] == 2:
        return 6
    elif count[0] == 3:
        return 3
    elif count[0] == 2 and count[1] == 2:
        return 2
    elif count[0] == 2:
        return 1
    else:
        return 0


def is_unique_element(hand):
    """Returns a boolean that checks if all items in the list are unique."""
    return len(hand) == len(set(hand))


def count_similar_iter(iterator):
    """Returns the elements of a list and their occurrences as a dictionary."""
    it = list(iterator)
    return {i: it.count(i) for i in it}


def hand_count(hand):
    """Returns the two highest occurrences of poker hand values."""
    count = count_similar_iter(hand_value(hand)).values()
    return sorted(count, reverse=True)[:2]


def hand_is_straight(hand):
    """Checks if all elements of a list of poker cards form a sequence."""
    sort_values = sorted(hand_value(hand))
    return sort_values == list(range(min(sort_values), max(sort_values)+1))


def high_card(hand):
    """Returns the maximum numeric value from a list of poker cards."""
    return max(hand_value(hand))


def hand_is_flush(hand):
    """Checks if all items in a poker card list have the same color."""
    return max(count_similar_iter(hand_color(hand)).values()) == len(hand)


def earnings(score, bet, vpoker_env):
    """Returns score information based on score and poker rules."""
    multiplier = vpoker_env.earn_multiplier(score)
    return bet * (multiplier-1), multiplier, vpoker_env.hand_name(score)


def view_earnings(mult, name):
    """Display score of your hand on screen."""
    if mult == 1:
        print("You have a {}, you keep your bet.".format(name))
    elif mult != 0:
        print("You have a {}, you win {} times your bet.".format(name, mult))
    else:
        print("You have a {}, you lose your bet.".format(name))
    return 0


def earn_calcul(hand, bet, vpoker_env):
    """Calculate the poker hand score and return the associated winnings."""
    score = poker_score(hand)
    earn, multiplier, score_name = earnings(score, bet, vpoker_env)
    view_earnings(multiplier, score_name)
    return earn
