from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Daniel Heuser'

doc = """
'Big5' Financial Literacy questions
"""

# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #
class Constants(BaseConstants):
    name_in_url = 'FinLit'
    players_per_group = None
    num_rounds = 1

# ******************************************************************************************************************** #
# *** CLASS SUBSESSIONS *** #
# ******************************************************************************************************************** #
class Subsession(BaseSubsession):
    pass

# ******************************************************************************************************************** #
# *** CLASS GROUPS *** #
# ******************************************************************************************************************** #
class Group(BaseGroup):
    pass

# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #
class Player(BasePlayer):
    interest_compounding = models.IntegerField()
    real_interest = models.IntegerField()
    diversification = models.IntegerField()
    bond_pricing = models.IntegerField()
    credit_interest = models.IntegerField()
