from forex_python.converter import CurrencyRates
from get import *
from choice import *
from convert import *
from historique import *
# import sys

country_names = get_country_names()
print(country_names)

while True:
# if len(sys.argv) <= 2:
    state_enter = choices_enter(country_names)
    state_output = choices_enter(country_names)
    amount = choices_amount()
# else:
#     state_enter = sys.argv[1]
#     state_output = sys.argv[2]
#     amount = float(sys.argv[3])

    rate = get_country_rates(state_enter, state_output)
    total = convert(amount, rate, state_output)
    total_print = (f"Pour {amount} {state_enter} vous récupererez {total}")
    print(total_print)
    # historique(total_print)
