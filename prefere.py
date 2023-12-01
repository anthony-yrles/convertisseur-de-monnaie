from fichier import *

def new_country(json_list, json):
    autorised_char = ["o", "n"]
    while True:
        new_country = input("Voulez-vous ajouter une devise ? (o/n):")
        while new_country not in autorised_char:
            new_country = input("Entrée non autorisée. Voulez-vous faire un autre calcul ? (o/n): ")
        if new_country.lower() == "o":
            new_country = input("Quelle devise voulez-vous ajouter? : ")
            if new_country in json_list:
                print("Cette devise existe déjà")
            new_rates = input("Quel est le taux de cette devise : ")
            json_list[new_country] = float(new_rates)
            save_to_json(json_list, json)
            print(f"la devise {new_country} à bien été ajouté au taux {new_rates}")
            return json_list
        else:
            return json_list

def prefered_country(preferences, prefered_choice, json_list, json):
    autorised_char = ["o", "n"]
    create_preference = input("Voulez-vous ajouter une devise à vos préférences ? (o/n): ")
    while create_preference not in autorised_char:
        create_preference = input("Entrée non autorisée. Voulez-vous faire un autre calcul ? (o/n): ")
    if create_preference.lower() == "o":
        print(preferences)
        pre_selected_preference = input("Votre devise préférée est-elle dans la liste ? (o/n): ")
        while pre_selected_preference not in autorised_char:
            pre_selected_preference = input("Entrée non autorisée. Voulez-vous faire un autre calcul ? (o/n): ")
        if pre_selected_preference.lower() == "o":
            selected_preference = input("Merci de donner le code à de votre devise favorite : ")
            if selected_preference in preferences:
                prefered_choice.append({selected_preference: preferences[selected_preference]})
                save_to_json(prefered_choice, json)
                print(f"La devise {selected_preference} a été ajoutée à vos préférences.")
            else:
                print(f"La devise {selected_preference} n'est pas dans la liste.")
                new_country(json_list, json)
                prefered_country(preferences, prefered_choice, json)
        else:
            new_country(json_list, json)
            prefered_country(json_list, prefered_choice, json)
