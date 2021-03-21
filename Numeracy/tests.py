from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):
        # ------------------------------------------------------------------------------------------------------------ #
        # make decisions
        # ------------------------------------------------------------------------------------------------------------ #
        yield (pages.SubIntro)
        yield (pages.Numeracy, {'fivesided_dice' : random.choice([1, 2, 3, -1]),
                              'variable_2' : random.choice([2, 3, 1, -1]),
                              'variable_3' : random.choice([2, 1, -1]),
                              'variable_4' : random.choice([2, 1, 3, 4, -1]),
                              'variable_5' : random.choice([1, 2, -1])})
