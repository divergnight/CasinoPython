# -*- coding: utf-8 -*-
from random import sample

from InputError import EmptyInputError, CardIndexError


def remove_element_iter(iterator, elem):
    """Removes all items from one iterator that are contained in another."""
    return list(filter(lambda x: x not in elem, iterator)), elem


def draw(iterator, elem=[], n=5):
    """Pull without replacement from a list until you get n cards."""
    hand = elem + sample(iterator, n-len(elem))
    return remove_element_iter(iterator, hand)


def view_hand(draw, vpoker_env):
    """Display a poker hand on screen."""
    print("\nYour hand :")
    for i, card in enumerate(draw):
        value, color = vpoker_env.card_name(card)
        print("  {} - {} of {}".format(i+1, value, color))
    print("")
    return 0


def type_list(iterator, type=int):
    """Changes all elements of a list to the format passed as an argument."""
    return list(map(type, iterator))


def move_one_to_another_list(old, new, idx):
    """Moves an item from one list to another based on an index."""
    return ([x for i, x in enumerate(old) if i != idx],
            new + [x for i, x in enumerate(old) if i == idx]
            )


def move_all_to_another_list(old, new, idx):
    """Moves multiple items from one list to another from an index list."""
    return ([x for i, x in enumerate(old) if i not in idx],
            new + [x for i, x in enumerate(old) if i in idx]
            )


def choice_keep_card(draw, table, n=5):
    """Move all cards from one list to another based on user input."""
    print(
        "Which card do you want to discard ?"
        "\n  - To indicate multiple cards, separate them with commas."
        " (eq: 1,4,5)"
        "\n  - To indicate discarding no cards, return a 0."
        )
    while True:
        try:
            res = input("").strip()
            if len(res) == 0:
                raise EmptyInputError
            if res == "0":
                return draw, table
            elif len(res) == 1:
                return move_one_to_another_list(draw, table, int(res)-1)
            else:
                res_list = list(map(lambda x: x-1, type_list(res.split(','))))
                if any(map(lambda x: x not in range(n), res_list)):
                    raise CardIndexError
                return move_all_to_another_list(draw, table, res_list)

        except EmptyInputError:
            print("Please enter your choice.")
        except CardIndexError:
            print("Please enter only numbers between 1 and 5.")
        except ValueError:
            print("Unknown value, please check your input.")


def machine(vpoker_env):
    """Executes two successive draws with rejection of a poker round"""
    deck = vpoker_env.deck()

    # Execute first draw
    deck, hand = draw(deck, [])
    view_hand(hand, vpoker_env)

    # Discard chosen cards
    hand, no = choice_keep_card(hand, [])

    # Execute second draw
    deck, hand = draw(deck, hand)
    view_hand(hand, vpoker_env)

    # Returns the hand score
    return hand
