from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models

# ******************************************************************************************************************** #
# *** PAGE Demographics *** #
# ******************************************************************************************************************** #

class Demographics(Page):
    form_model = models.Player
    form_fields = ["age", "gender", "stock_ownership", "risk_attitude", "stats_knowledge"]

    def vars_for_template(self):
        # specify info for task progress
        section = int(3)
        section_total = int(4)
        section_progress = int(section / section_total * 100)

        # specify info for progress bar
        total = Constants.num_rounds
        page = self.subsession.round_number
        progress = int(page / total * 100)

        return {
            'section': section,
            'section_total': section_total,
            'section_progress': section_progress,
            'page': page,
            'total': total,
            'progress': progress,
        }





page_sequence = [Demographics]
