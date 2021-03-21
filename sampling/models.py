from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv
import random

author = """
Christoph Huber
"""

doc = """
Sampling Returns and Price Developments - 'Volatility shocks and investment behavior'
"""


class Constants(BaseConstants):
    name_in_url = 'sampling'
    players_per_group = None
    num_rounds = 18

    time_per_return = 500

    riskfree = 0.9

    initial_wealth = 5000

    # --- Load Data 1 from .csv ---
    with open("sampling/static/sampling/data" + str(1) + "_new1" + ".csv") as datacsv:
        prices1 = []
        returns1 = []
        reader = csv.reader(datacsv, delimiter=';')
        next(reader)
        for row in reader:
            prices1.append(row[0])
            returns1.append(row[1])

    # --- Load Data 2 from .csv ---
    with open("sampling/static/sampling/data" + str(2) + "_new1" + ".csv") as datacsv:
        prices2 = []
        returns2 = []
        reader = csv.reader(datacsv, delimiter=';')
        next(reader)
        for row in reader:
            prices2.append(row[0])
            returns2.append(row[1])

    # --- Load Data 3 from .csv ---
    with open("sampling/static/sampling/data" + str(3) + "_new1" + ".csv") as datacsv:
        prices3 = []
        returns3 = []
        reader = csv.reader(datacsv, delimiter=';')
        next(reader)
        for row in reader:
            prices3.append(row[0])
            returns3.append(row[1])

    # --- Load Data 4 from .csv ---
    with open("sampling/static/sampling/data" + str(4) + "_new1" + ".csv") as datacsv:
        prices4 = []
        returns4 = []
        reader = csv.reader(datacsv, delimiter=';')
        next(reader)
        for row in reader:
            prices4.append(row[0])
            returns4.append(row[1])

    # --- Load Data 5 from .csv ---
    with open("sampling/static/sampling/data" + str(5) + "_new1" + ".csv") as datacsv:
        prices5 = []
        returns5 = []
        reader = csv.reader(datacsv, delimiter=';')
        next(reader)
        for row in reader:
            prices5.append(row[0])
            returns5.append(row[1])

    # --- Load Data 6 from .csv ---
    with open("sampling/static/sampling/data" + str(6) + "_new1" + ".csv") as datacsv:
        prices6 = []
        returns6 = []
        reader = csv.reader(datacsv, delimiter=';')
        next(reader)
        for row in reader:
            prices6.append(row[0])
            returns6.append(row[1])

    #    prices = [i[0] for i in prices]
    prices1 = [float(i) for i in prices1]
    prices2 = [float(i) for i in prices2]
    prices3 = [float(i) for i in prices3]
    prices4 = [float(i) for i in prices4]
    prices5 = [float(i) for i in prices5]
    prices6 = [float(i) for i in prices6]

    #    returns = [i[0] for i in returns]
    returns1 = [float(i) for i in returns1]
    returns2 = [float(i) for i in returns2]
    returns3 = [float(i) for i in returns3]
    returns4 = [float(i) for i in returns4]
    returns5 = [float(i) for i in returns5]
    returns6 = [float(i) for i in returns6]

    # --- Load Monthly Returns from .csv ---
    with open("sampling/static/sampling/mreturns_new.csv") as datacsv:
        mreturns = []
        reader = csv.reader(datacsv, delimiter=';')
        next(reader)
        for row in reader:
            mreturns.append(row)

    mreturns1 = [i[0] for i in mreturns]
    mreturns2 = [i[1] for i in mreturns]
    mreturns3 = [i[2] for i in mreturns]
    mreturns4 = [i[3] for i in mreturns]
    mreturns5 = [i[4] for i in mreturns]
    mreturns6 = [i[5] for i in mreturns]
    mreturns1 = [float(i) for i in mreturns1]
    mreturns2 = [float(i) for i in mreturns2]
    mreturns3 = [float(i) for i in mreturns3]
    mreturns4 = [float(i) for i in mreturns4]
    mreturns5 = [float(i) for i in mreturns5]
    mreturns6 = [float(i) for i in mreturns6]


class Subsession(BaseSubsession):

    def creating_session(self):
        if self.round_number == 1:
            for p in self.get_players():
                p.participant.vars['count'] = []

                p.participant.vars['treatment_returns'] = random.choice([0, 1])
                p.treatment_returns = p.participant.vars['treatment_returns']

                block = [1]
                round = [0]
                month = [0]
                init_wealth = [Constants.initial_wealth]
                percentage = [0]
                end_wealth = [Constants.initial_wealth]
                mreturn = [0]
                ownreturn = [0]
                history = list(zip(block, round, month, init_wealth, percentage, end_wealth, mreturn, ownreturn))
                p.participant.vars['history'] = history

                # DEFINE RETURNS / PRICES FOR EACH SUBJECT
                # p.random_data = random.randint(1, 6)

                p.participant.vars['path'] = [1, 2, 3]
                random.shuffle(p.participant.vars['path'])
                p.path = p.participant.vars['path'][0]
                p.pathvar = random.choice([1, 2])
                p.participant.vars['pathvarinit'] = p.pathvar

                p.random_initialvalue = random.randint(40 * 100, (60+1) * 100) / 10000

                if p.participant.vars['path'][0] == 1:
                    if p.pathvar == 1:
                        returns = Constants.returns1.copy()
                        prices = [i * p.random_initialvalue for i in Constants.prices1.copy()]
                        mreturns = Constants.mreturns1.copy()
                    elif p.pathvar == 2:
                        returns = Constants.returns2.copy()
                        prices = [i * p.random_initialvalue for i in Constants.prices2.copy()]
                        mreturns = Constants.mreturns2.copy()

                elif p.participant.vars['path'][0] == 2:
                    if p.pathvar == 1:
                        returns = Constants.returns3.copy()
                        prices = [i * p.random_initialvalue for i in Constants.prices3.copy()]
                        mreturns = Constants.mreturns3.copy()
                    elif p.pathvar == 2:
                        returns = Constants.returns4.copy()
                        prices = [i * p.random_initialvalue for i in Constants.prices4.copy()]
                        mreturns = Constants.mreturns4.copy()

                elif p.participant.vars['path'][0] == 3:
                    if p.pathvar == 1:
                        returns = Constants.returns5.copy()
                        prices = [i * p.random_initialvalue for i in Constants.prices5.copy()]
                        mreturns = Constants.mreturns5.copy()
                    elif p.pathvar == 2:
                        returns = Constants.returns6.copy()
                        prices = [i * p.random_initialvalue for i in Constants.prices6.copy()]
                        mreturns = Constants.mreturns6.copy()

                p.participant.vars['returns'] = returns
                p.participant.vars['prices'] = prices
                p.participant.vars['mreturns'] = mreturns


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    treatment_returns = models.IntegerField(blank=True)

    random_initialvalue = models.FloatField(blank=True)

    investment = models.FloatField(blank=True)
    rate = models.IntegerField(blank=True)
    risk = models.IntegerField(blank=True)
    fc = models.FloatField(blank=True)
    fc_p05 = models.FloatField(blank=True)
    fc_p95 = models.FloatField(blank=True)
    satisfaction = models.IntegerField(blank=True)

    monthly_return = models.FloatField(blank=True)

    path = models.IntegerField(blank=True)
    pathvar = models.IntegerField(blank=True)

    def write_history(self):
        block, round, month, init_wealth, percentage, end_wealth, mreturn, ownreturn = list(zip(*self.participant.vars['history']))

        if self.round_number < 6:
            block = block + (1,)
            round = round + (self.round_number,)
            month = month + (self.round_number,)
            init_wealth = init_wealth + (end_wealth[self.round_number - 1],)
            percentage = percentage + (self.investment,)
            end_wealth = end_wealth + (init_wealth[self.round_number] * (1 + self.participant.vars['mreturns'][self.round_number - 1] * self.investment / 100),)
            mreturn = mreturn + (self.participant.vars['mreturns'][self.subsession.round_number - 1] * 100,)
            ownreturn = ownreturn + (self.participant.vars['mreturns'][self.round_number - 1] * self.investment,)

        elif self.round_number == 6:
            block = block + (2,)
            round = round + (self.round_number,)
            month = month + (self.round_number - 6,)
            init_wealth += (Constants.initial_wealth,)
            percentage += (0,)
            end_wealth += (Constants.initial_wealth,)
            mreturn += (0,)
            ownreturn += (0,)

        elif self.round_number > 6 and self.round_number < 12:
            block = block + (2,)
            round = round + (self.round_number,)
            month = month + (self.round_number - 6,)
            init_wealth = init_wealth + (end_wealth[self.round_number - 1],)
            percentage = percentage + (self.investment,)
            end_wealth = end_wealth + (init_wealth[self.round_number] * (1 + self.participant.vars['mreturns'][self.round_number - 7] * self.investment / 100),)
            mreturn = mreturn + (self.participant.vars['mreturns'][self.subsession.round_number - 7] * 100,)
            ownreturn = ownreturn + (self.participant.vars['mreturns'][self.round_number - 7] * self.investment,)

        elif self.round_number == 12:
            block = block + (3,)
            round = round + (self.round_number,)
            month = month + (self.round_number - 12,)
            init_wealth += (Constants.initial_wealth,)
            percentage += (0,)
            end_wealth += (Constants.initial_wealth,)
            mreturn += (0,)
            ownreturn += (0,)

        elif self.round_number > 12 and self.round_number < Constants.num_rounds:
            block = block + (3,)
            round = round + (self.round_number,)
            month = month + (self.round_number - 12,)
            init_wealth = init_wealth + (end_wealth[self.round_number - 1],)
            percentage = percentage + (self.investment,)
            end_wealth = end_wealth + (init_wealth[self.round_number] * (1 + self.participant.vars['mreturns'][self.round_number - 13] * self.investment / 100),)
            mreturn = mreturn + (self.participant.vars['mreturns'][self.subsession.round_number - 13] * 100,)
            ownreturn = ownreturn + (self.participant.vars['mreturns'][self.round_number - 13] * self.investment,)

        self.participant.vars['history'] = list(zip(block, round, month, init_wealth, percentage, end_wealth, mreturn, ownreturn))

    def write_variables(self):
        if self.round_number < 7:
            if self.subsession.round_number - 2 >= 0:
                self.monthly_return = self.participant.vars['mreturns'][self.round_number - 2]
            else:
                self.monthly_return = -9999
        elif self.round_number >= 7 and self.round_number < 13:
            if self.round_number - 8 >= 0:
                self.monthly_return = self.participant.vars['mreturns'][self.round_number - 8]
            else:
                self.monthly_return = -9999
        elif self.round_number >= 13:
            if self.round_number - 14 >= 0:
                self.monthly_return = self.participant.vars['mreturns'][self.round_number - 14]
            else:
                self.monthly_return = -9999

    def reset_path(self):

        if self.subsession.round_number == 7 or self.subsession.round_number == 13:

            self.random_initialvalue = random.randint(40 * 100, (60+1) * 100) / 10000

            self.path = self.participant.vars['path'][int(self.subsession.round_number/6)]

            if self.subsession.round_number == 12:
                self.pathvar = random.choice([1, 2])
            elif self.participant.vars['pathvarinit'] == 1:
                self.pathvar = 2
            elif self.participant.vars['pathvarinit'] == 2:
                self.pathvar = 1

            if self.participant.vars['path'][int(self.subsession.round_number/6)] == 1:
                if self.pathvar == 1:
                    returns = Constants.returns1.copy()
                    prices = [i * self.random_initialvalue for i in Constants.prices1.copy()]
                    mreturns = Constants.mreturns1.copy()
                elif self.pathvar == 2:
                    returns = Constants.returns2.copy()
                    prices = [i * self.random_initialvalue for i in Constants.prices2.copy()]
                    mreturns = Constants.mreturns2.copy()

            elif self.participant.vars['path'][int(self.subsession.round_number/6)] == 2:
                if self.pathvar == 1:
                    returns = Constants.returns3.copy()
                    prices = [i * self.random_initialvalue for i in Constants.prices3.copy()]
                    mreturns = Constants.mreturns3.copy()
                elif self.pathvar == 2:
                    returns = Constants.returns4.copy()
                    prices = [i * self.random_initialvalue for i in Constants.prices4.copy()]
                    mreturns = Constants.mreturns4.copy()

            elif self.participant.vars['path'][int(self.subsession.round_number/6)] == 3:
                if self.pathvar == 1:
                    returns = Constants.returns5.copy()
                    prices = [i * self.random_initialvalue for i in Constants.prices5.copy()]
                    mreturns = Constants.mreturns5.copy()
                elif self.pathvar == 2:
                    returns = Constants.returns6.copy()
                    prices = [i * self.random_initialvalue for i in Constants.prices6.copy()]
                    mreturns = Constants.mreturns6.copy()

            self.participant.vars['returns'] = returns
            self.participant.vars['prices'] = prices
            self.participant.vars['mreturns'] = mreturns
