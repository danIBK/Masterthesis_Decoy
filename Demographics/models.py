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
This app asks for demographics and some basic variables
"""


class Constants(BaseConstants):
    name_in_url = 'Demographics'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='Wie alt sind Sie?', min=13, max=125)
    gender = models.StringField(
        # choices=[['Mann', 'Mann'], ['Frau', 'Frau'], ['Andere', 'Andere']],
        # label='Welches Geschlecht sind sie?',
        # widget=widgets.RadioSelect,
    )
    stock_ownership = models.BooleanField(
        # label="Besitzen Sie Aktien/Fonds oder sonstige Finanzinstrumente",
        # choices=[[True, "Ja"],
        #          [False, "Nein"]],
        # widget = widgets.RadioSelect,
    )
    stats_knowledge = models.StringField(
        # label="Wie würden Sie Ihr Wissen über Statistik beschreiben",
        # choices = ["Anfänger", "Basis", "Fortgeschritten", "Experte"],
        # widget = widgets.RadioSelectHorizontal,
    )
    risk_attitude= models.IntegerField(
        # label='Wie schätzen Sie sich persönlich ein: Sind Sie im allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden? ☞ Bitte kreuzen Sie ein Kästchen auf der Skala an, wobei der Wert 0 bedeutet: "gar nicht risikobereit" und der Wert 10: "sehr risikobereit". Mit den Werten dazwischen können Sie Ihre Einschätzung abstufen',
        # choices=[1,2,3,4,5,6,7,8,9,10],
        # widget=widgets.RadioSelectHorizontal,
    )

