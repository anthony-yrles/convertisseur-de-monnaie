from forex_python.converter import CurrencyRates
from get import *
from choice import *
from convert import *
from historique import *
from prefere import *
from fichier import *
from fav_use import *

country_data = get_country_data()
json_name = 'annexe_date.json'
country_json = save_to_json(country_data, json_name)
preferences = read_to_json(json_name)
historical = []
prefered_choice = []
json_fav = 'annexe_fav.json'
country_fav = save_to_json(prefered_choice, json_fav)
favs = read_to_json(json_fav)

while True:
    autorised_char = ["o", "n"]
    create_preference = input("Voulez-vous ajouter une devise à vos favoris ? (o/n): ")
    while create_preference not in autorised_char:
        create_preference = input("Entrée non autorisée. Voulez-vous ajouter une devise à vos favoris ? (o/n): ")
    if create_preference.lower() == "o":
        prefered_country(preferences, prefered_choice, country_json, json_fav, autorised_char)

    new_currency = input("Voulez-vous ajouter une devise à la liste normal? (o/n): ")
    while new_currency not in autorised_char:
        new_currency = input("Entrée non autorisée. Voulez-vous ajouter une devise à la liste normal? (o/n): ")
    if new_currency.lower() == "o":    
        new_country(preferences, json_name)
    
    country_names = get_country_names(country_json)
    fav_use = input("Voulez-vous utiliser une devise favorite ? (o/n): ")
    while fav_use not in autorised_char:
        fav_use = input("Entrée non autorisée. Voulez-vous utiliser une devise favorite ? (o/n): ")
    if fav_use == "o":
        fav(json_fav, country_names)
    else:
        print(f"Voiçi la liste des devise existante : {country_names}")
        state_enter = choices_enter(country_names)
        state_output = choices_enter(country_names)
        amount = choices_amount()
        rate = get_country_rates(country_json, state_enter, state_output)
        total = convert(amount, rate, state_output)
        total_print = f"Pour {amount} {state_enter} vous récupérerez {total} \n"

    print(total_print)

    historical = historique(historical, total_print)


