from objets import Grille, Cellule
from time import sleep

if __name__ == "__main__":
    jeu = Grille()
#    dictionnaire_cellules = {}
#    cle_dict_cellule = 1
#    for ligne in range(9):
#        for colonne in range(9):
#            dictionnaire_cellules[cle_dict_cellule] = Cellule(jeu, ligne, colonne)
#            cle_dict_cellule += 1

    while any([cell_value == " " for cell_value in sum(jeu.cellules_organisees, [])]):
        jeu.display()
#        for ligne in range(9):
#            for cellule in jeu.cellules_organisees[ligne]:
#                cellule = Cellule(jeu, ligne, jeu.cellules_organisees[ligne].index(cellule))

        for cellule in jeu.infos_cellules.values():
            print(f"Cellule : {cellule.position} ; Possibilities : {cellule.possibilities}")
            if cellule.valeur != " ":
                cellule.possibilities = []
            else:
                cellule.first_verification(jeu)
                if cellule.valeur == " ":
                    cellule.second_verification(jeu)
#                    if cellule.valeur == " ":
#                        cellule.third_verification(jeu)
            cellule.update_valeurs(jeu.cellules_organisees)
        
        print()
        print()
        print()
#        sleep(20)
        continuer = input("Entrer pour continuer")

    jeu.display()

