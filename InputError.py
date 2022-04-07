# -*- coding: utf-8 -*-
class Error(Exception):
    """Base class for other exceptions"""
    pass


class BetTooHighError(Error):
    """The bet must be less than the bankroll."""
    pass


class EmptyInputError(Error):
    """Please enter your choice."""
    pass


class CardIndexError(Error):
    """Please enter only numbers between 1 and 5."""
    pass


class IllegalHand(Error):
    """The hand cannot have multiple copies of the same card."""
    pass
