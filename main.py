from time import sleep
from collections import Counter

from objets import Grille


if __name__ == "__main__":
    jeu = Grille()
    jeu.display()
    try_version = 0
    fork_version_work = False
#    print(jeu)  # /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
    while any([cell_value.valeur == " " for cell_value in sum(jeu.grille_updated, [])]):
#        print("BOUCLE PRINCIPALE !!!")
        grille_intermediaire_avant = [[cellule.valeur for cellule in jeu.grille_updated[i]] for i in range(9)]
#        print(grille_intermediaire_avant)  # /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
#        print(jeu.grille_updated)  # /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
        for cellule in sum(jeu.grille_updated, []):
            cellule.update_valeurs(jeu)
#            print(f"CELLULE : {cellule.position} ; Valeur : {cellule.valeur} ; Possibilities : {cellule.possibilities}")  # /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
            if cellule.valeur != " ":
                cellule.possibilities = []
            else:
                cellule.first_verification(jeu)
                if cellule.valeur == " ":
                    cellule.second_verification(jeu)
                    if cellule.valeur == " ":
                        cellule.third_verification(jeu)

        grille_intermediaire_apres = [[cellule.valeur for cellule in jeu.grille_updated[i]] for i in range(9)]
#        print(grille_intermediaire_apres)  # /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*

        if grille_intermediaire_apres == grille_intermediaire_avant and try_version > 3:
#            print("TENTATIVE RISQUEE !!!")
            try_version = True
            values = grille_intermediaire_apres
            fork_version = Grille(values)
#            print(f"The fork_version is : {fork_version}")  # /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
#            fork_version.display()
            possibilities_occurencies_descending = []
            key_cell_ligne = -1
            key_cell_colonne = -1
            for cellule in sum(fork_version.grille_updated, []):
                if cellule.valeur != " ":
                    cellule.possibilities = []
                else:
                    cellule.first_verification(fork_version)
                    if cellule.valeur == " ":
                        cellule.second_verification(fork_version)
                        if cellule.valeur == " ":
                            cellule.third_verification(fork_version)
#                print(cellule.possibilities)
                if len(cellule.possibilities) == 2:
                    possibilities_occurencies_descending.extend(cellule.possibilities)
            possibilities_occurencies_descending = [i for i in Counter(possibilities_occurencies_descending).keys()]
#            print(possibilities_occurencies_descending)  # /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
            central_square_cells = sum([[fork_version.grille_updated[ligne][colonne] for colonne in range(3,6)] for ligne in range(3,6)], [])
            central_lignes_cells = sum([fork_version.grille_updated[ligne] for ligne in range(3,6)], [])
            central_colonnes_cells = sum([[fork_version.grille_updated[ligne][colonne] for colonne in range(3, 6)] for ligne in range(9)], [])
            key_cell_in_square = False

            most_missing_duo = possibilities_occurencies_descending[:2]
#            print(most_missing_duo)  # /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
            for cellule in central_square_cells:
                if cellule.possibilities == most_missing_duo or cellule.possibilities == most_missing_duo[::-1]:
                    key_cell_in_square = True
                    key_cell_ligne = cellule.numero_ligne
                    key_cell_colonne = cellule.numero_colonne
                    cellule.valeur = most_missing_duo[0]
                    alternative = most_missing_duo[1]
                    break
            if key_cell_in_square == False:
                for cellule in sum([central_lignes_cells, central_colonnes_cells], []):
                    if cellule.possibilities == most_missing_duo or cellule.possibilities == most_missing_duo[::-1]:
                        key_cell_ligne = cellule.numero_ligne
                        key_cell_colonne = cellule.numero_colonne
                        cellule.valeur = most_missing_duo[0]
                        alternative = most_missing_duo[1]
                        break
            print(f"key_cell best case : ({key_cell_ligne}, {key_cell_colonne})")

            if key_cell_ligne == -1 and key_cell_colonne == -1:
                most_missing_duo = possibilities_occurencies_descending[1:3]
#                print(most_missing_duo)  # /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
                for cellule in central_square_cells:
                    if cellule.possibilities == most_missing_duo or cellule.possibilities == most_missing_duo[::-1]:
                        key_cell_in_square = True
                        key_cell_ligne = cellule.numero_ligne
                        key_cell_colonne = cellule.numero_colonne
                        cellule.valeur = most_missing_duo[0]
                        alternative = most_missing_duo[1]
                        break
                if key_cell_in_square == False:
                    for cellule in sum([central_lignes_cells, central_colonnes_cells], []):
                        if cellule.possibilities == most_missing_duo or cellule.possibilities == most_missing_duo[::-1]:
                            key_cell_ligne = cellule.numero_ligne
                            key_cell_colonne = cellule.numero_colonne
                            cellule.valeur = most_missing_duo[0]
                            alternative = most_missing_duo[1]
                            break
                print(f"key_cell second best case : ({key_cell_ligne}, {key_cell_colonne})")
            
            run_number = 0
            fork_version_work = True
            while any([cell_value.valeur == " " for cell_value in sum(fork_version.grille_updated, [])]):
                grille_intermediaire_fork_avant = [[cellule.valeur for cellule in fork_version.grille_updated[i]] for i in range(9)]
                for cellule in sum(fork_version.grille_updated, []):
                    cellule.update_valeurs(fork_version)
#                print(f"CELLULE : {cellule.position} ; Valeur : {cellule.valeur} ; Possibilities : {cellule.possibilities}")  # /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*
                    if cellule.valeur != " ":
                        cellule.possibilities = []
                    else:
                        cellule.first_verification(fork_version)
                        if cellule.valeur == " ":
                            cellule.second_verification(fork_version)
                            if cellule.valeur == " ":
                                cellule.third_verification(fork_version)
                grille_intermediaire_fork_apres = [[cellule.valeur for cellule in fork_version.grille_updated[i]] for i in range(9)]
                run_number += 1
#                print(run_number)
                if grille_intermediaire_fork_apres == grille_intermediaire_fork_avant and run_number > 1:
                    fork_version_work = False
                    jeu.grille_updated[key_cell_ligne][key_cell_colonne].valeur = alternative
                    break
#            fork_version.display()
#            continuer = input("Entrer pour continuer")
        if fork_version_work:
            break

        else:
            try_version += 1
#            print(f"try_version : {try_version}")


#        jeu.display()
#        continuer = input("Entrer pour continuer")
#        sleep(5)
print()
print()
# continuer = input("Entrer pour continuer")
if fork_version_work:
    fork_version.display()
else:
    jeu.display()


