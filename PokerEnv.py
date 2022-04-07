# -*- coding: utf-8 -*-
class PokerEnv:
    """Contains data and its methods related to a poker game.

    In case of modification of this environment, only this class will be
    modified.
    """
    __hand_name = [
        "High card",
        "Pair",
        "Two pair",
        "Three of a kind",
        "Straight",
        "Flush",
        "Full House",
        "Four of a kind",
        "Straight Flush",
        "Royal Flush",
    ]
    __deck = [
        '{}-{}'.format((x, '10')[x == 'X'], y)
        for y in "hdcs" for x in '23456789XJQKA'
        ]
    __value_name = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": "Jack",
        "Q": "Queen",
        "K": "King",
        "A": "Ace",
    }
    __color_name = {
        "h": "Hearths",
        "d": "Diamonds",
        "c": "Clubs",
        "s": "Spares"
    }

    def hand_name(self, n):
        """Returns the literal value of a poker hand given a score."""
        return self.__hand_name[n]

    def card_name(self, card):
        """Returns the pair of corresponding literal values of a poker card."""
        value, color = card.split("-")
        return (self.__value_name[value], self.__color_name[color])

    def deck(self):
        """Returns the list of all cards in a poker deck"""
        return self.__deck
