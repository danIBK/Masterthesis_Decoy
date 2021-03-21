from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from . import models

# copy of FinLit maybe it overwrites some important files###
# ******************************************************************************************************************** #
# *** PAGE SUB INTRO *** #
# ******************************************************************************************************************** #


class SubIntro(Page):
    # time out
    # ----------------------------------------------------------------------------------------------------------------
    timeout_seconds = 10
    timer_text = "Verbleibende Zeit bis du automatisch weitergeleitet wirst:"


# ******************************************************************************************************************** #
# *** PAGE Numeracy *** #
# ******************************************************************************************************************** #
# specify form models and form fields
class Numeracy(Page):
    form_model = models.Player
    form_fields = ['fivesided_dice', 'chor', 'loaded_dice'
                   ]

    def vars_for_template(self):
        # specify info for task progress
        section = int(2)
        section_total = int(4)
        section_progress = int(section / section_total * 100)

        # specify info for progress bar
        total = int(2)
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


page_sequence = [Numeracy]
