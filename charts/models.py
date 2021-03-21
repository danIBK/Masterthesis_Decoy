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
import csv
import random


author = 'Daniel Heuser'

doc = """
Base setting and treatment setting for allocation choice of financial decisions with decoy
"""


class Constants(BaseConstants):
    name_in_url = 'charts'
    players_per_group = None
    num_rounds = 1

    # --- Load Data 1 from .csv ---
    with open("charts/static/data" + str(1) + "_new1" + ".csv") as datacsv:
        prices1 = []
        returns1 = []
        reader = csv.reader(datacsv, delimiter=';')
        next(reader)
        for row in reader :
            prices1.append(row[0])
            returns1.append(row[1])

    #    prices = [i[0] for i in prices]
    prices1 = [float(i) for i in prices1]

    #    returns = [i[0] for i in returns]
    returns1 = [float(i) for i in returns1]

    # --- Load Generate R data from .csv ---
    with open("charts/static/charts/returns_generateR.csv") as datacsv :
        returnsrandom = []
        reader = csv.reader(datacsv, delimiter=';')
        next(reader)
        for row in reader :
            returnsrandom.append(row[0])
            # pricesrandom.append(row[0])


    #    prices = [i[0] for i in prices]
    returnsrandom = [float(i) for i in returnsrandom]

    returnstest = [100,100.728887, 101.1138416,
99.62266837,98.84948156,98.30885145,99.32738692,99.38950129,100.1269033,100.7019981,98.17088058,98.65163123,100.5015558,
100.4419982,100.5996784,101.1614084,101.6966077,102.1725642,101.8806494,101.931042,102.6223688,102.9047041,102.4349912,
103.2068161,103.4264703,103.5129962,100.6416727,99.41362586,99.95648687,101.5195469,101.564071,99.91315079,100.3014818,
102.1340341,101.6192821,100.1845365,100.9167422,100.4027809,98.53562314,99.06645015,98.5309278,97.29604405,94.17298631,
87.27992257,85.10320971,76.44956612,81.30687435,86.95104798,84.92997376,83.48491458,79.7026858,84.77326504,82.89927682,
86.12289297,88.07742849,90.27240154,86.24676503,84.44781318,84.74182816,86.9137149,83.48975306,83.06454607,83.47131979,
83.21606033,83.53949503,83.98953553,83.87906432,83.92055294,84.05513071,83.02947568,84.1942551,83.37860489,84.68242985,
83.10761837,82.4626074,82.91290517,83.30095091,83.28870221,83.72934513,84.34128693,84.79353646,83.54304645,83.57968647,
83.82093678,82.77041269,83.37643589,83.84199444,84.16241255,84.29453605,81.95630906,81.08399183,80.82373932,80.38683138,
80.87531615,80.99987803,81.24793865,81.44485431,80.99941403,80.63301564,79.32232898,79.09569901,
          ]




class Subsession(BaseSubsession):
    pass





class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatment = models.BooleanField()

    ##################################
    # Base decission variables  #
    ##################################
    percentage_rf = models.FloatField()
    percentage_market = models.FloatField()

    ##################################
    # Treatment decission variables  #
    ##################################
    tm_percentage_rf = models.FloatField()
    tm_percentage_market = models.FloatField()
    tm_percentage_decoy = models.FloatField()

    sum_percentage = models.FloatField(blank=True)

    market_return_B = models.FloatField()
    market_return_T = models.FloatField()

    total_return_B = models.FloatField()
    total_return_T = models.FloatField()

    base_or_treatment = models.BooleanField()
    final_return = models.FloatField()




