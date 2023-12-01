from forex_python.converter import CurrencyRates
from get import *
from choice import *
from convert import *
from historique import *
from prefere import *
from fichier import *

historical = []
prefered_choice = []
country_data = get_country_data()
json_name = 'annexe_date.json'
json_fav = 'annexe_fav.json'
country_json = save_to_json(country_data, json_name)
preferences = read_to_json(json_name)

while True:
    prefered_country(preferences, prefered_choice, country_json, json_fav)
    new_country(preferences, json_name)

    country_names = get_country_names(country_data)
    state_enter = choices_enter(country_names)
    state_output = choices_enter(country_names)
    amount = choices_amount()

    rate = get_country_rates(country_data, state_enter, state_output)
    total = convert(amount, rate, state_output)
    total_print = f"Pour {amount} {state_enter} vous récupérerez {total} \n"
    print(total_print)

    historical = historique(historical, total_print)


