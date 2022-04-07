# -*- coding: utf-8 -*-
from PokerEnv import PokerEnv


class VideoPokerEnv(PokerEnv):
    """Contains data and its methods related to a video poker game.
    This class inherits from the poker class.

    In case of modification of this environment, only this class will be
    modified.
    """
    __earn_multiplier = [0, 1, 2, 3, 4, 6, 9, 25, 50, 250]

    def earn_multiplier(self, n: int):
        """Returns the multiplier of a bet given a score."""
        return self.__earn_multiplier[n]
