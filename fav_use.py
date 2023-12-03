from convert import *
from choice import *
from get import *

def fav(json_fav, country_names):
    while True:
        fav_name = input("Quel devise favorite voulez vous choisir? : ")
        while fav_name not in json_fav:
            print(json_fav)
            fav_name = input("Entrée non autorisée. Veuillez selectionner un pays qui est dans la liste: ")
        amount = choices_amount()
        state_output = choices_enter(country_names)
        rate = get_country_rates(json_fav, fav_name, state_output)
        total = convert(amount, rate, state_output)
        total_print = f"Pour {amount} {fav_name} vous récupérerez {total} \n"
        return(total_print)
        
        
