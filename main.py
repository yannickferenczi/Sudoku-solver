from objets import Grille, Cellule
from time import sleep

if __name__ == "__main__":
    jeu = Grille()
    dictionnaire_cellules = {}
    cle_dict_cellule = 1
    for ligne in range(9):
        for colonne in range(9):
            dictionnaire_cellules[cle_dict_cellule] = Cellule(jeu, ligne, colonne)
            cle_dict_cellule += 1

    while any([cell_value == " " for cell_value in sum(jeu.cellules_organisees, [])]):
        jeu.display()
#        for ligne in range(9):
#            for cellule in jeu.cellules_organisees[ligne]:
#                cellule = Cellule(jeu, ligne, jeu.cellules_organisees[ligne].index(cellule))

        for cellule in dictionnaire_cellules.values():
            if cellule.valeur != " ":
                cellule.possibilities = []
            else:
                cellule.first_verification(jeu)
                cellule.second_verification(jeu)
#                cellule.third_verification(jeu, dictionnaire_cellules)
                cellule.valeurs_square_appartenance, cellule.valeurs_lignes_par_3, cellule.valeurs_colonnes_par_3 = cellule.determine_valeurs_square_lignes_par_3_colonnes_par_trois(jeu)

            print(f"Cellule : {cellule.position} ; Possibilities : {cellule.possibilities}")
#            print(f"Positions colonnes_par_3 = {cellule.positions_colonnes_par_3} || Positions lignes_par_3 = {cellule.positions_lignes_par_3}")

        
        print()
        print()
        print()
#        sleep(20)
        continuer = input("Entrer pour continuer")
