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
            yield (pages.FinLit, {'interest_compounding': random.choice([1,2,3,-1]),
                                  'real_interest': random.choice([2,3,1,-1]),
                                  'diversification': random.choice([2,1,-1]),
                                  'bond_pricing': random.choice([2,1,3,4,-1]),
                                  'credit_interest': random.choice([1,2,-1])})

