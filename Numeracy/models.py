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
Berlin Numeracy Test from Cokely et al.(2012).
"""


# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #
class Constants(BaseConstants):
    name_in_url = 'Numeracy'
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
    fivesided_dice = models.IntegerField()
    chor = models.IntegerField()
    loaded_dice = models.IntegerField()
