from objets import Grille
from time import sleep

if __name__ == "__main__":
    jeu = Grille()
    jeu.display()
#    print(jeu)
    while any([cell_value.valeur == " " for cell_value in sum(jeu.grille_updated, [])]):
#        print(jeu.grille_updated)  # ----------------------------------------------------------------------------
        for cellule in sum(jeu.grille_updated, []):
#            print(f"CELLULE : {cellule.position} ; Valeur : {cellule.valeur} ; Possibilities : {cellule.possibilities}")
            if cellule.valeur != " ":
                cellule.possibilities = []
            else:
                cellule.first_verification(jeu)
                if cellule.valeur == " ":
                    cellule.second_verification(jeu)
#                    if cellule.valeur == " ":
#                        cellule.third_verification(jeu)
            cellule.update_valeurs(jeu)
#        sleep(20)
print()
print()
continuer = input("Entrer pour continuer")
jeu.display()


