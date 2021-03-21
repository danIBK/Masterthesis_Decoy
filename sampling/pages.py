from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from django.utils.translation import ugettext as _


class Sampling(Page):

    form_model = 'player'
    form_fields = [
        'investment',
        'rate',
        'risk',
        'fc',
        'fc_p05',
        'fc_p95',
        'satisfaction'
    ]

    def is_displayed(self):
        return self.player.participant.vars['treatment_returns'] == 1

    def vars_for_template(self):

        if self.subsession.round_number < 7:
            page = self.subsession.round_number - 1
            if page-1 >= 0:
                mreturn = self.player.participant.vars['mreturns'][self.subsession.round_number - 2] * 100
            else:
                mreturn = -9999
            history = self.player.participant.vars['history']

        elif self.subsession.round_number >= 7 and self.subsession.round_number < 13:
            page = self.subsession.round_number - 7
            if page-1 >= 0:
                mreturn = self.player.participant.vars['mreturns'][self.subsession.round_number - 8] * 100
            else:
                mreturn = -9999
            history = self.player.participant.vars['history'][6:]

        elif self.subsession.round_number >= 13:
            page = self.subsession.round_number - 13
            if page-1 >= 0:
                mreturn = self.player.participant.vars['mreturns'][self.subsession.round_number - 14] * 100
            else:
                mreturn = -9999
            history = self.player.participant.vars['history'][12:]

        return {
            'prices': self.player.participant.vars['prices'],
            'returns': self.player.participant.vars['returns'],
            'page': page,
            'part': history[0][0],
            'num_pages': Constants.num_rounds - 1,
            'history': history,
            'init_wealth': self.player.participant.vars['history'][page][1],
            'end_wealth': self.player.participant.vars['history'][page][3],
            'mreturns': self.player.participant.vars['mreturns'],
            'mreturn': mreturn
        }

    def before_next_page(self):
        self.player.write_variables()
        self.player.reset_path()
        self.player.write_history()


class Sampling1(Page):

    form_model = 'player'
    form_fields = [
        'investment',
        'rate',
        'risk',
        'fc',
        'fc_p05',
        'fc_p95',
        'satisfaction'
    ]

    def is_displayed(self):
        return self.player.participant.vars['treatment_returns'] == 0

    def vars_for_template(self):

        if self.subsession.round_number < 7:
            page = self.subsession.round_number - 1
            if page-1 >= 0:
                mreturn = self.player.participant.vars['mreturns'][self.subsession.round_number - 2] * 100
            else:
                mreturn = -9999
            history = self.player.participant.vars['history']

        elif self.subsession.round_number >= 7 and self.subsession.round_number < 13:
            page = self.subsession.round_number - 7
            if page-1 >= 0:
                mreturn = self.player.participant.vars['mreturns'][self.subsession.round_number - 8] * 100
            else:
                mreturn = -9999
            history = self.player.participant.vars['history'][6:]

        elif self.subsession.round_number >= 13:
            page = self.subsession.round_number - 13
            if page-1 >= 0:
                mreturn = self.player.participant.vars['mreturns'][self.subsession.round_number - 14] * 100
            else:
                mreturn = -9999
            history = self.player.participant.vars['history'][12:]

        return {
            'prices': self.player.participant.vars['prices'],
            'returns': self.player.participant.vars['returns'],
            'page': page,
            'part': history[0][0],
            'num_pages': Constants.num_rounds - 1,
            'history': history,
            'init_wealth': self.player.participant.vars['history'][self.subsession.round_number - 1][1],
            'end_wealth': self.player.participant.vars['history'][self.subsession.round_number - 1][3],
            'mreturns': self.player.participant.vars['mreturns'],
            'mreturn': mreturn
        }

    def before_next_page(self):
        self.player.write_variables()
        self.player.reset_path()
        self.player.write_history()


class Sampling2(Page):

    def is_displayed(self):
        False

    def vars_for_template(self):

        page = self.subsession.round_number - 1
        returns1 = Constants.returns1[0:(page*30-1)]

        count0 = sum(1 for i in returns1 if i <= -4.0)
        count1 = sum(1 for i in returns1 if i > -4.0 and i <= -3.0)
        count2 = sum(1 for i in returns1 if i > -3.0 and i <= -2.0)
        count3 = sum(1 for i in returns1 if i > -2.0 and i <= -1.0)
        count4 = sum(1 for i in returns1 if i > -1.0 and i < 0)
        count5 = sum(1 for i in returns1 if i >= 0 and i <= 1.0)
        count6 = sum(1 for i in returns1 if i > 1.0 and i <= 2.0)
        count7 = sum(1 for i in returns1 if i > 2.0 and i <= 3.0)
        count8 = sum(1 for i in returns1 if i > 3.0 and i <= 4.0)
        count9 = sum(1 for i in returns1 if i > 4.0)

        return {
            'returns': Constants.returns1,
            'page': self.subsession.round_number,
            'count': [
                count0,
                count1,
                count2,
                count3,
                count4,
                count5,
                count6,
                count7,
                count8,
                count9
            ],
            'count0': count0,
            'count1': count1,
            'count2': count2,
            'count3': count3,
            'count4': count4,
            'count5': count5,
            'count6': count6,
            'count7': count7,
            'count8': count8,
            'count9': count9
        }




class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Sampling,
    Sampling1,
    # Sampling2
]
