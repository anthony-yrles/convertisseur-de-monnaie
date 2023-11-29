def choices_enter (country_names):
    while True:
        state_enter = input("Merci de préciser la devise que vous voulez convertir : ")
        for i in country_names:
            if state_enter in country_names:
                return(state_enter)
            else:
                state_enter = input("Merci de sélectionner un pays valide : ")

def choices_output (country_names):
    while True:
        state_output = input("Merci de préciser la devise que vous voulez en retour : ")
        for i in country_names:
            if state_output in country_names:
                return(state_output)
            else:
                state_output = input("Merci de sélectionner un pays valide : ")

def choices_amount():
    while True:
        try:
            amount = float(input("Combien voulez-vous convertir ? : "))
            break
        except ValueError:
            print("Merci d'entrer un nombre valide.")

    return amount