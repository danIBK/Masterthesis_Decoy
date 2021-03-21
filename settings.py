from os import environ

SESSION_CONFIGS = [
    dict(
        name='Numeracy',
        display_name="Numeracy Test",
        num_demo_participants=3,
        app_sequence=['Numeracy'],
    ),
    dict(
        name='FinLit',
        display_name='Financial Literacy',
        num_demo_participants=3,
        app_sequence=['FinLit', 'payment_info'],
    ),
    dict(
        name='Demographics',
        display_name='Demographics, Stock Ownership, Risk Attitude and Statistical Knowledge',
        num_demo_participants=3,
        app_sequence=['Demographics'],
    ),
    # dict(
    #     name='sampling',
    #     display_name='sampling',
    #     num_demo_participants=3,
    #     app_sequence=['sampling'],
    # ),
    dict(
        name='charts',
        display_name='charts',
        num_demo_participants=3,
        app_sequence=['charts'],
    ),
    dict(
        name='Master_Thesis',
        display_name='Experiment Daniel Heuser',
        num_demo_participants=3,
        app_sequence=[
            # 'charts',
            'introduction', 'charts', 'FinLit', 'Numeracy', 'Demographics', 'Outro'],
    ),
    dict(
        name='Introduction',
        display_name='Introduction',
        num_demo_participants=1,
        app_sequence=[
            'introduction'
        ],
    ),
    dict(
        name='Outro',
        display_name='Thank You Page',
        num_demo_participants=1,
        app_sequence=[
            'Outro'
        ],
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.00, participation_fee=10.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'de'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
]

# AUTH_LEVEL:
# this setting controls which parts of your site are freely accessible,
# and which are password protected:
# - If it's not set (the default), then the whole site is freely accessible.
# - If you are launching a study and want visitors to only be able to
#   play your app if you provided them with a start link, set it to STUDY.
# - If you would like to put your site online in public demo mode where
#   anybody can play a demo version of your game, but not access the rest
#   of the admin interface, set it to DEMO.

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games. This is a trial run by a uibk.student.
"""

SECRET_KEY = '=3+*47nu4%-ja-k2+7*-e7#h%r-@rx(sn5-n^vqpd*qix(t_m$'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
# INSTALLED_APPS = ['otree',]
INSTALLED_APPS = ['otree', 'django.contrib.humanize']  #
