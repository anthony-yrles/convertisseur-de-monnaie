from convert import *

def fav(json):
    autorised_char = ["o", "n"]
    while True:
        fav_use = input("Voulez-vous utiliser une devise favorite ? (o/n): ")
        while fav_use not in autorised_char:
            fav_use = input("Entrée non autorisée. Voulez-vous utiliser une devise favorite ? (o/n): ")
        fav_name = input("Quel devise favorite voulez vous choisir? : ")
        while fav_name not in json:
            print(json)
            fav_name = input("Entrée non autorisée. Veuillez selectionner un pays qui est dans la liste: ")
        convert()
        
        
