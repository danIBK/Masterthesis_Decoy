from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models


class ThankYou(Page):
    form_model = models.Player
    form_fields = ['comments',
                   ]


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [ThankYou]
