# -*- coding: utf-8 -*-
from os import system as cmd
from VideoPokerEnv import VideoPokerEnv

from InputError import BetTooHighError, EmptyInputError
from poker_draw import machine
from poker_earn import earn_calcul


def view_bankroll(earn, bet, bankroll):
    """Display status of your bankroll."""
    print("Your bankroll : {} $ ({})".format(bankroll + earn, earn))
    return 0


def input_bankroll():
    """Gets and returns bankroll value from user input."""
    while True:
        try:
            bankroll = input(
                "Enter the total amount you want to play with (in $) :\n"
                )
            if len(bankroll) > 0:
                return int(bankroll)
            else:
                print('Please enter your choice.')
        except ValueError:
            print("Unknown value, please check your input.")


def input_bet(bankroll):
    """Gets and returns bet value from user input."""
    while True:
        try:
            res = input(
                "Enter the stake with which you want to"
                " play this round (in $) :\n"
                )
            if len(res) == 0:
                raise EmptyInputError
            bet = int(res)
            if bet > bankroll:
                raise BetTooHighError
        except EmptyInputError:
            print("Please enter your choice.")
        except BetTooHighError:
            print("The bet must be less than the bankroll.")
        except ValueError:
            print("Unknown value, please check your input.")
        else:
            return bet


def input_continue():
    return input("Do you want to play again ? (y: yes, any: no)\n") == 'y'


def party(bet, bankroll, vpoker_env):
    """Play a game of video poker according to video poker rules."""
    hand = machine(vpoker_env)
    earn = earn_calcul(hand, bet, vpoker_env)

    view_bankroll(earn, bet, bankroll)

    return bankroll + earn


def video_poker():
    """Play a complete game of video poker according to video poker rules."""
    vpoker_env = VideoPokerEnv()

    bankroll = input_bankroll()

    while True:
        bet = input_bet(bankroll)

        bankroll = party(bet, bankroll, vpoker_env)

        if bankroll <= 0:
            print(
                "You have no more money, looking forward to"
                " seeing you again."
                )
            break

        if not input_continue():
            break
        cmd('cls')


def main(*args, debug=True):
    """Runs the main program, catching any unexpected interrupts."""
    try:
        video_poker()
    except KeyboardInterrupt:  # (exit code 3221225786)
        return 15
    except Exception as msg:
        if debug:
            raise msg
        else:
            return 1


if __name__ == '__main__':
    main(debug=True)
