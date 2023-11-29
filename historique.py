def historique(save_calcul):
    autorised_char =["o", "n"]
    continue_break = input("Voulez-vous faire un autre calcul ? (o/n): ")
    if continue_break not in autorised_char:
        continue_break = input("Entrée non autorisé. Voulez-vous faire un autre calcul ? (o/n): ")
    elif continue_break == "n":
        histo = input("Voulez-vous afficher l'historique ? (o/n): ")
        if histo not in autorised_char:
            histo = input("Entrée non autorisé. Voulez-vous faire un autre calcul ? (o/n): ")
        elif histo == "o":
            # for calc in save_calcul:
            print(f"Calculs effectués : {save_calcul}")