START_HELP = """Commands:
/help - help text
/add - add item
    command args:
        cost(int | float) -- ietm cost: 12 12.34;
        name(str) -- name of item;
        (ortional)
        category(int | str) -- category id or name;
        date(int) -- number of day back: -1 -2;
/confirm - confirm adding;
/cancel - cancel adding;
"""

CONFIRM_SUCCESS = "Confirm success"
CANCEL_SUCCESS = "Cancel success"
ITEM = "{category} {name} = {cost:.2f} {date:%Y-%m-%d}"

ERROR = "Something went wrong" 
WRONG_PARAMETERS_NUMBER_ERROR = "Wrong parameters number"
WRONG_COST_ERROR = "Wrong cost, cost should be int or float number"
WRONG_CAREGORY_ERROR = "Wrong category, category should be id or name"
