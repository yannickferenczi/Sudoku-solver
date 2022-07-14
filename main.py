from objets import Colonne_par_3, Grille, Cellule, Ligne_par_3
from time import sleep

if __name__ == "__main__":
    jeu = Grille()
    dictionnaire_cellules = {}
    cle_dict_cellule = 1
    for ligne in range(9):
        for colonne in range(9):
            dictionnaire_cellules[cle_dict_cellule] = Cellule(jeu, ligne, colonne)
            cle_dict_cellule += 1
    
    a_b_c = Ligne_par_3(jeu, range(3))
    d_e_f = Ligne_par_3(jeu, range(3, 6))
    g_h_i = Ligne_par_3(jeu, range(6, 9))

    i_ii_iii = Colonne_par_3(jeu, range(3))
    iv_v_vi = Colonne_par_3(jeu, range(3, 6))
    vii_viii_ix = Colonne_par_3(jeu, range(6, 9))

    while any([cell_value == " " for cell_value in sum(jeu.cellules_organisees, [])]):
        jeu.display()
        for ligne in range(9):
            for cellule in jeu.cellules_organisees[ligne]:
                cellule = Cellule(jeu, ligne, jeu.cellules_organisees[ligne].index(cellule))

        for cellule in dictionnaire_cellules.values():
            cellule.verification(jeu)
        
        print()
        print()
        print()
        sleep(3)
