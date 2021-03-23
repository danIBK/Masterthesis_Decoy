from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models
import random


class Explain(Page):
    form_model = models.Player
    form_fields = []

    def vars_for_template(self):
        # specify info for task progress
        section = int(1)
        section_total = int(4)
        section_progress = int(section / section_total * 100)

        # specify info for page progress bar
        total = int(4)
        page = int(1)
        progress = int(page / total * 100)

        # Random Number
        number_B = random.randint(1, 100)
        number_T = random.randint(1, 100)

        #
        self.player.market_return_B = Constants.returnsrandom[number_B]
        self.player.market_return_T = Constants.returnsrandom[number_T]

        return {
            'section': section,
            'section_total': section_total,
            'section_progress': section_progress,
            'page': page,
            'total': total,
            'progress': progress,
            'number_B': number_B,
            'number_T': number_T,
        }

class Quiz(Page):
    form_model = models.Player
    form_fields = [
        'quiz_vola1',
        'quiz_vola2',
        'quiz_vola3',
        'quiz_vola4',
        'quiz_cor1',
        'quiz_cor2',
        'quiz_cor3',
        'quiz_cor4',
    ]

    def vars_for_template(self):
        # specify info for task progress
        section = int(1)
        section_total = int(4)
        section_progress = int(section / section_total * 100)

        # specify info for page progress bar
        total = int(5)
        page = int(2)
        progress = int(page / total * 100)

        return {
            'section': section,
            'section_total': section_total,
            'section_progress': section_progress,
            'page': page,
            'total': total,
            'progress': progress,
        }

    def error_message(self, values):
        solutions = dict(
            quiz_vola1=None,
            quiz_vola2=1,
            quiz_vola3=1,
            quiz_vola4=None,
            quiz_cor1=1,
            quiz_cor2=None,
            quiz_cor3=None,
            quiz_cor4=1,
        )

        error_messages = dict(
        )

        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Nicht Korrekt. Lesen Sie die Hinweise wenn Sie sich unsicher sind.'

        return error_messages



class charts(Page):
    form_model = models.Player
    form_fields = ['percentage_rf',
                   'percentage_market',
                   ]

    # @staticmethod
    # def error_message(player, values):
    #     print('values is', values)
    #     if values['percentage_rf'] + values['percentage_market'] != 100:
    #         return 'The numbers must add up to 100%'

    # @staticmethod
    # def investtherest(player, values):
    #     values['percentage_rf'] = float(1 -values['percentage_rf'])
    #     return values['percentage_rf']

    # def is_displayed(self):
    #     return: True
    #

    def vars_for_template(self):
        # specify info for task progress
        section = int(1)
        section_total = int(4)
        section_progress = int(section / section_total * 100)

        # specify info for progress bar
        total = int(4)
        page = int(2)
        progress = int(page / total * 100)

        # Random Number
        number_B = random.randint(1, 100)

        return {
            'section': section,
            'section_total': section_total,
            'section_progress': section_progress,
            'page': page,
            'total': total,
            'progress': progress,
            'number_B': number_B,

        }

    def js_vars(player):
        numbers = Constants.returnstest
        highcharts_series = player.round_number
        return highcharts_series


class treatmentpage(Page):
    form_model = models.Player
    form_fields = ['tm_percentage_rf', 'tm_percentage_decoy',
                    'tm_percentage_market',
                   'sum_percentage'
                   ]
    def error_message(self, values):
            print('values is', values)
            if values['tm_percentage_rf'] + values['tm_percentage_decoy'] + values['tm_percentage_market'] != 100:
                return 'Stellen Sie sicher dass Sie genau 100% der 10000€ verteilt haben'


    # @staticmethod
    # def error_message(player, values) :
    #     print('values is', values)
    #     if values['tm_percentage_rf'] + values['tm_percentage_decoy'] + values['tm_percentage_market'] != 100:
    #         return 'The numbers must add up to 100%'



    def vars_for_template(self) :
        # specify info for task progress
        section = int(1)
        section_total = int(4)
        section_progress = int(section / section_total * 100)

        # specify info for page progress bar
        total = int(4)
        page = int(3)
        progress = int(page / total * 100)

        number_T = random.randint(1,100)


        # sum_percent = sum(self.player.participant.vars['tm_percentage_rf'], self.player.participant.vars['tm_percentage_decoy'], self.player.participant.vars['tm_percentage_market'])


        return {
            'section': section,
            'section_total': section_total,
            'section_progress': section_progress,
            'page': page,
            'total': total,
            'progress': progress,
            'number_T': number_T,
            # 'sum_percent' : sum_percent
        }



class ResultsWaitPage(WaitPage):
    pass




class Results(Page):




    def vars_for_template(self):
        # specify info for task progress
        section = int(1)
        section_total = int(4)
        section_progress = int(section / section_total * 100)

        # specify info for page progress bar
        total = int(4)
        page = int(4)
        progress = int(page / total * 100)

        costs_Decoy = 0.005
        costs_Market = 0.0025
        total_return_B = 0
        total_return_T = 0
        self.player.total_return_B = \
            round(10000 * (self.player.percentage_rf*0.05 +
                           self.player.percentage_market * (self.player.market_return_B - costs_Market)
                           ) / 100
                  , 2)

        self.player.total_return_T = \
            round(10000 * (self.player.tm_percentage_rf*0.05 +
                           self.player.tm_percentage_market * (self.player.market_return_T - costs_Market) +
                           self.player.tm_percentage_decoy * (self.player.market_return_T - costs_Decoy)
                           ) / 100
                  , 2)
        base_or_treatment = random.randint(0, 1)
        final_return = -9999
        self.player.base_or_treatment = base_or_treatment
        payment_list = [self.player.total_return_B, self.player.total_return_T]
        self.player.final_return = payment_list[base_or_treatment]
        self.player.payoff = 0.0014*(payment_list[base_or_treatment])+0.562


        return {
            'section': section,
            'section_total': section_total,
            'section_progress': section_progress,
            'page': page,
            'total': total,
            'progress': progress,
            'total_return_B': total_return_B,
            'total_return_T': total_return_T,
            'base_or_treatment': base_or_treatment,
            'final_return': final_return,
        }



# def vars_for_template(self):
    #     result1 = self.player.in_all_rounds()
    #     payoff1 = 0
    #     for player in result1:
    #         payoff1 += player.payoff
    #     return {
    #         'payoff1': payoff1
    #     }


page_sequence = [Explain, Quiz, charts, treatmentpage, Results]
