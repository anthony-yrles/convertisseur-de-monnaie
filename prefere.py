from fichier import *

def new_country(json_list, json_file):
    while True:
        new_currency = input("Quelle devise voulez-vous ajouter? : ")
        if new_currency in json_list:
            print("Cette devise existe déjà")
        else:
            new_rates = input("Quel est le taux de cette devise : ")
            json_list[new_currency] = float(new_rates)
            save_to_json(json_list, json_file)
            print(f"La devise {new_currency} a bien été ajoutée au taux {new_rates}")
            return json_list

def prefered_country(preferences, prefered_choice, json_list, json, autorised_char):
    print(preferences)
    pre_selected_preference = input("Votre devise préférée est-elle dans la liste ? (o/n): ")
    while pre_selected_preference not in autorised_char:
        pre_selected_preference = input("Entrée non autorisée. Voulez-vous faire un autre calcul ? (o/n): ")
    if pre_selected_preference.lower() == "o":
        selected_preference = input("Merci de donner le code à de votre devise favorite : ")
        if selected_preference in preferences:
            prefered_choice.append({selected_preference: preferences[selected_preference]})
            country_fav = save_to_json(prefered_choice, json)
            print(f"La devise {selected_preference} a été ajoutée à vos préférences.")
            return(country_fav)
        else:
            print(f"La devise {selected_preference} n'est pas dans la liste.")
