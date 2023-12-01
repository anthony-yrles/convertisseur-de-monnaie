def historique(save_calcul, new_entry):
    autorised_char = ["o", "n"]

    continue_break = input("Voulez-vous faire un autre calcul ? (o/n): ")

    while continue_break not in autorised_char:
        continue_break = input("Entrée non autorisée. Voulez-vous faire un autre calcul ? (o/n): ")

    if continue_break == "n":
        histo = input("Voulez-vous afficher l'historique ? (o/n): ")

        while histo not in autorised_char:
            histo = input("Entrée non autorisée. Voulez-vous afficher l'historique ? (o/n): ")

        if histo == "o":
            print("Calculs effectués :", end="")
            for calc in save_calcul:
                print(calc, end="")
            print(new_entry)
    return save_calcul + [new_entry]