
class Grille:
    def __init__(self):
        """
        self.valeurs_initiales = [  # difficulté : easy ; Solutionné (vérifications 1 et 2 suffisent) ----------------------------------------------
            ["3", "8", " ", "9", " ", " ", "2", " ", "5"],
            [" ", " ", " ", " ", " ", "8", "7", "3", " "],
            [" ", "6", " ", "3", " ", " ", "9", "8", " "],
            [" ", " ", " ", " ", " ", "3", "5", " ", "1"],
            ["9", "1", " ", "5", " ", "7", " ", "2", "3"],
            ["7", " ", "3", "1", " ", " ", " ", " ", " "],
            [" ", "3", "5", " ", " ", "1", " ", "9", " "],
            [" ", "7", "4", "6", " ", " ", " ", " ", " "],
            ["8", " ", "1", " ", " ", "2", " ", "6", "7"]
        ]
        """
        
        self.valeurs_initiales = [  # difficulté : medium ; Pas solutionné ----------------------------------------------
            ["9", " ", "7", "8", " ", " ", " ", "6", " "],
            [" ", " ", "6", "7", " ", " ", "1", "8", " "],
            [" ", "1", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", "8", " ", " ", "4", " ", " ", " "],
            ["1", " ", " ", " ", "5", " ", " ", " ", "3"],
            [" ", " ", " ", " ", "9", " ", " ", "7", "8"],
            [" ", " ", " ", " ", "1", " ", " ", " ", " "],
            ["6", " ", " ", "4", " ", " ", " ", " ", "5"],
            ["5", " ", " ", " ", " ", "9", " ", " ", "1"]
        ]

        """
        self.valeurs_initiales = [  # difficulté : medium ; Solutionné (vérification 1, 2 et 3 suffisent) ----------------------------------------------
            [" ", " ", "7", " ", " ", "5", " ", " ", "9"],
            [" ", " ", " ", " ", " ", "8", " ", " ", " "],
            ["2", " ", "5", "7", "3", " ", " ", " ", " "],
            ["3", " ", "9", "2", "1", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", "4"],
            ["8", " ", " ", " ", "9", "3", " ", " ", " "],
            [" ", "7", " ", " ", " ", " ", "3", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", "9", " "],
            [" ", " ", "2", " ", "8", " ", "6", " ", "1"]
        ]
        """

        """
        self.valeurs_initiales = [  # difficulté : easy ; Solutionné (vérifications 1 et 2 suffisent) ----------------------------------------------
            ["5", "3", " ", " ", "7", " ", " ", " ", " "],
            ["6", " ", " ", "1", "9", "5", " ", " ", " "],
            [" ", "9", "8", " ", " ", " ", " ", "6", " "],
            ["8", " ", " ", " ", "6", " ", " ", " ", "3"],
            ["4", " ", " ", "8", " ", "3", " ", " ", "1"],
            ["7", " ", " ", " ", "2", " ", " ", " ", "6"],
            [" ", "6", " ", " ", " ", " ", "2", "8", " "],
            [" ", " ", " ", "4", "1", "9", " ", " ", "5"],
            [" ", " ", " ", " ", "8", " ", " ", "7", "9"]
        ]
        """

        self.positions_cellules = []
        for ligne in range(9):
            positions_cellules_dans_ligne = []
            for colonne in range(9):
                position_cellule = (str(ligne), str(colonne))
                positions_cellules_dans_ligne.append(position_cellule)
            self.positions_cellules.append(positions_cellules_dans_ligne)

        self.grille_updated = [[Cellule(self.valeurs_initiales, self.positions_cellules, ligne, colonne) for colonne in range(9)] for ligne in range(9)]

#        print(self.grille_updated)  # ----------------------------------------------------------------------------
#        print(sum(self.grille_updated, []))  # ----------------------------------------------------------------------------

        
    def display(self):
        for row in self.grille_updated:
            print(f"| {' | '.join(row[i].valeur for i in range(9))} |")
            print("-"*37)

"""
class Ligne_par_3:
    def __init__(self, jeu, numero_lignes):
        self.liste_valeurs_cellules = sum([jeu.valeurs_initiales[i] for i in numero_lignes], [])
        self.valeurs_ligne_haute = jeu.valeurs_initiales[numero_lignes[0]]
        self.valeurs_ligne_milieu = jeu.valeurs_initiales[numero_lignes[1]]
        self.valeurs_ligne_basse = jeu.valeurs_initiales[numero_lignes[2]]

        self.liste_positions_cellules = sum([jeu.positions_cellules[i] for i in numero_lignes[0:3]], [])
        self.positions_ligne_haute = jeu.positions_cellules[numero_lignes[0]]
        self.positions_ligne_milieu = jeu.positions_cellules[numero_lignes[1]]
        self.positions_ligne_basse = jeu.positions_cellules[numero_lignes[2]]

class Colonne_par_3:
    def __init__(self, jeu, numero_colonnes):
        self.liste_valeurs_cellules = sum([jeu.valeurs_initiales[i][(numero_colonnes[0:3])] for i in range(9)], [])
        self.valeurs_colonne_left = sum([jeu.valeurs_initiales[i][numero_colonnes[0]] for i in range(9)], [])
        self.valeurs_colonne_milieu = sum([jeu.valeurs_initiales[i][numero_colonnes[1]] for i in range(9)], [])
        self.valeurs_colonne_right = sum([jeu.valeurs_initiales[i][numero_colonnes[2]] for i in range(9)], [])

        self.liste_positions_cellules = sum([jeu.positions_cellules[i][(numero_colonnes[0:3])] for i in range(9)], [])
        self.positions_colonne_left = sum([jeu.positions_cellules[i][numero_colonnes[0]] for i in range(9)], [])
        self.positions_colonne_milieu = sum([jeu.positions_cellules[i][numero_colonnes[1]] for i in range(9)], [])
        self.positions_colonne_right = sum([jeu.positions_cellules[i][numero_colonnes[2]] for i in range(9)], [])
"""

class Cellule:
    def __init__(self, valeurs_initiales, positions_cellules, numero_ligne, numero_colonne):
        self.position = (str(numero_ligne), str(numero_colonne))
        self.numero_ligne = numero_ligne
        self.numero_colonne = numero_colonne
        self.valeur = valeurs_initiales[self.numero_ligne][self.numero_colonne]
        self.possibilities = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] if self.valeur == " " else []
        self.valeurs_ligne_appartenance = valeurs_initiales[self.numero_ligne]
        self.positions_ligne_appartenance = positions_cellules[self.numero_ligne]
        self.valeurs_colonne_appartenance = [valeurs_initiales[i][self.numero_colonne] for i in range(9)]
        self.positions_colonne_appartenance = [positions_cellules[i][self.numero_colonne] for i in range(9)]
        self.positions_square_appartenance, self.positions_lignes_par_3, self.positions_colonnes_par_3 = self.determine_positions_square_lignes_par_3_colonnes_par_trois(positions_cellules)
        self.valeurs_square_appartenance, self.valeurs_lignes_par_3, self.valeurs_colonnes_par_3 = self.determine_valeurs_square_lignes_par_3_colonnes_par_trois(valeurs_initiales)

    def update_valeurs(self, jeu):
#        print(jeu)  # ----------------------------------------------------------------------------
#        print([[jeu.grille_updated[ligne][colonne].valeur for colonne in range(9)] for ligne in range(9)])
        valeurs_updated = [[jeu.grille_updated[ligne][colonne].valeur for colonne in range(9)] for ligne in range(9)]
        self.valeur = jeu.grille_updated[self.numero_ligne][self.numero_colonne].valeur
#        print(self.valeur)  # ----------------------------------------------------------------------------
        self.valeurs_ligne_appartenance = [jeu.grille_updated[self.numero_ligne][i].valeur for i in range(9)]
        self.valeurs_colonne_appartenance = [jeu.grille_updated[i][self.numero_colonne].valeur for i in range(9)]
        self.valeurs_square_appartenance, self.valeurs_lignes_par_3, self.valeurs_colonnes_par_3 = self.determine_valeurs_square_lignes_par_3_colonnes_par_trois(valeurs_updated)
#        print(self.valeurs_square_appartenance, self.valeurs_lignes_par_3, self.valeurs_colonnes_par_3)  # ----------------------------------------------------------------------------


    def determine_positions_square_lignes_par_3_colonnes_par_trois(self, positions_cellules):
        if self.numero_ligne <= 2:
            positions_lignes_par_3 = [positions_cellules[i] for i in range(3)]
            if self.numero_colonne <= 2:
                positions_square = sum([positions_cellules[i][:3] for i in range(3)], [])
                positions_colonnes_par_3 = [[positions_cellules[i][0] for i in range(9)], [positions_cellules[i][1] for i in range(9)], [positions_cellules[i][2] for i in range(9)]]
            elif 3 <= self.numero_colonne <= 5:
                positions_square = sum([positions_cellules[i][3:6] for i in range(3)], [])
                positions_colonnes_par_3 = [[positions_cellules[i][3] for i in range(9)], [positions_cellules[i][4] for i in range(9)], [positions_cellules[i][5] for i in range(9)]]
            elif 6 <= self.numero_colonne:
                positions_square = sum([positions_cellules[i][6:9] for i in range(3)], [])
                positions_colonnes_par_3 = [[positions_cellules[i][6] for i in range(9)], [positions_cellules[i][7] for i in range(9)], [positions_cellules[i][8] for i in range(9)]]
        elif 3 <= self.numero_ligne <= 5:
            positions_lignes_par_3 = [positions_cellules[i] for i in range(3, 6)]
            if self.numero_colonne <= 2:
                positions_square = sum([positions_cellules[i][:3] for i in range(3, 6)], [])
                positions_colonnes_par_3 = [[positions_cellules[i][0] for i in range(9)], [positions_cellules[i][1] for i in range(9)], [positions_cellules[i][2] for i in range(9)]]
            elif 3 <= self.numero_colonne <= 5:
                positions_square = sum([positions_cellules[i][3:6] for i in range(3, 6)], [])
                positions_colonnes_par_3 = [[positions_cellules[i][3] for i in range(9)], [positions_cellules[i][4] for i in range(9)], [positions_cellules[i][5] for i in range(9)]]
            elif 6 <= self.numero_colonne:
                positions_square = sum([positions_cellules[i][6:9] for i in range(3, 6)], [])
                positions_colonnes_par_3 = [[positions_cellules[i][6] for i in range(9)], [positions_cellules[i][7] for i in range(9)], [positions_cellules[i][8] for i in range(9)]]
        elif 6 <= self.numero_ligne:
            positions_lignes_par_3 = [positions_cellules[i] for i in range(6, 9)]
            if self.numero_colonne <= 2:
                positions_square = sum([positions_cellules[i][:3] for i in range(6, 9)], [])
                positions_colonnes_par_3 = [[positions_cellules[i][0] for i in range(9)], [positions_cellules[i][1] for i in range(9)], [positions_cellules[i][2] for i in range(9)]]
            elif 3 <= self.numero_colonne <= 5:
                positions_square = sum([positions_cellules[i][3:6] for i in range(6, 9)], [])
                positions_colonnes_par_3 = [[positions_cellules[i][3] for i in range(9)], [positions_cellules[i][4] for i in range(9)], [positions_cellules[i][5] for i in range(9)]]
            elif 6 <= self.numero_colonne:
                positions_square = sum([positions_cellules[i][6:9] for i in range(6, 9)], [])
                positions_colonnes_par_3 = [[positions_cellules[i][6] for i in range(9)], [positions_cellules[i][7] for i in range(9)], [positions_cellules[i][8] for i in range(9)]]
        return positions_square, positions_lignes_par_3, positions_colonnes_par_3

    def determine_valeurs_square_lignes_par_3_colonnes_par_trois(self, valeurs):
#        print(jeu)  # ----------------------------------------------------------------------------
        if self.numero_ligne <= 2:
            valeurs_lignes_par_3 = [valeurs[i] for i in range(3)]
            if self.numero_colonne <= 2:
                valeurs_square = sum([valeurs[i][:3] for i in range(3)], [])
                valeurs_colonnes_par_3 = [valeurs[i][:3] for i in range(9)]
            elif 3 <= self.numero_colonne <= 5:
                valeurs_square = sum([valeurs[i][3:6] for i in range(3)], [])
                valeurs_colonnes_par_3 = [valeurs[i][3:6] for i in range(9)]
            elif 6 <= self.numero_colonne:
                valeurs_square = sum([valeurs[i][6:9] for i in range(3)], [])
                valeurs_colonnes_par_3 = [valeurs[i][6:9] for i in range(9)]
        elif 3 <= self.numero_ligne <= 5:
            valeurs_lignes_par_3 = [valeurs[i] for i in range(3, 6)]
            if self.numero_colonne <= 2:
                valeurs_square = sum([valeurs[i][:3] for i in range(3, 6)], [])
                valeurs_colonnes_par_3 = [valeurs[i][:3] for i in range(9)]
            elif 3 <= self.numero_colonne <= 5:
                valeurs_square = sum([valeurs[i][3:6] for i in range(3, 6)], [])
                valeurs_colonnes_par_3 = [valeurs[i][3:6] for i in range(9)]
            elif 6 <= self.numero_colonne:
                valeurs_square = sum([valeurs[i][6:9] for i in range(3, 6)], [])
                valeurs_colonnes_par_3 = [valeurs[i][6:9] for i in range(9)]
        elif 6 <= self.numero_ligne:
            valeurs_lignes_par_3 = [valeurs[i] for i in range(6, 9)]
            if self.numero_colonne <= 2:
                valeurs_square = sum([valeurs[i][:3] for i in range(6, 9)], [])
                valeurs_colonnes_par_3 = [valeurs[i][:3] for i in range(9)]
            elif 3 <= self.numero_colonne <= 5:
                valeurs_square = sum([valeurs[i][3:6] for i in range(6, 9)], [])
                valeurs_colonnes_par_3 = [valeurs[i][3:6] for i in range(9)]
            elif 6 <= self.numero_colonne:
                valeurs_square = sum([valeurs[i][6:9] for i in range(6, 9)], [])
                valeurs_colonnes_par_3 = [valeurs[i][6:9] for i in range(9)]
        return valeurs_square, valeurs_lignes_par_3, valeurs_colonnes_par_3
    
    def first_verification(self, jeu):
#        print(jeu.grille_updated[0][0].valeurs_colonne_appartenance)# ----------------------------------------------------------------------------
        not_possible = []
        for possibility in self.possibilities:
            if possibility in self.valeurs_ligne_appartenance or possibility in self.valeurs_colonne_appartenance or possibility in self.valeurs_square_appartenance:
                not_possible.append(possibility)
        for solution in not_possible:
            self.possibilities.remove(solution)
        if len(self.possibilities) == 1 and self.valeur == " ":
            jeu.grille_updated[self.numero_ligne][self.numero_colonne].valeur = self.possibilities[0]

    def second_verification(self, jeu):
        if self.position in self.positions_lignes_par_3[0]:
            for possibility in self.possibilities:
                if possibility in self.valeurs_lignes_par_3[1] and possibility in self.valeurs_lignes_par_3[2]:
                    if self.position in self.positions_colonnes_par_3[0]:
                        if possibility in self.valeurs_colonnes_par_3[1] and possibility in self.valeurs_colonnes_par_3[2]:
                            jeu.grille_updated[self.numero_ligne][self.numero_colonne].valeur = possibility
                    elif self.position in self.positions_colonnes_par_3[1]:
                        if possibility in self.valeurs_colonnes_par_3[0] and possibility in self.valeurs_colonnes_par_3[2]:
                            jeu.grille_updated[self.numero_ligne][self.numero_colonne].valeur = possibility
                    elif self.position in self.positions_colonnes_par_3[2]:
                        if possibility in self.valeurs_colonnes_par_3[0] and possibility in self.valeurs_colonnes_par_3[1]:
                            jeu.grille_updated[self.numero_ligne][self.numero_colonne].valeur = possibility
        elif self.position in self.positions_lignes_par_3[1]:
            for possibility in self.possibilities:
                if possibility in self.valeurs_lignes_par_3[0] and possibility in self.valeurs_lignes_par_3[2]:
                    if self.position in self.positions_colonnes_par_3[0]:
                        if possibility in self.valeurs_colonnes_par_3[1] and possibility in self.valeurs_colonnes_par_3[2]:
                            jeu.grille_updated[self.numero_ligne][self.numero_colonne].valeur = possibility
                    elif self.position in self.positions_colonnes_par_3[1]:
                        if possibility in self.valeurs_colonnes_par_3[0] and possibility in self.valeurs_colonnes_par_3[2]:
                            jeu.grille_updated[self.numero_ligne][self.numero_colonne].valeur = possibility
                    elif self.position in self.positions_colonnes_par_3[2]:
                        if possibility in self.valeurs_colonnes_par_3[0] and possibility in self.valeurs_colonnes_par_3[1]:
                            jeu.grille_updated[self.numero_ligne][self.numero_colonne].valeur = possibility
        elif self.position in self.positions_lignes_par_3[2]:
            for possibility in self.possibilities:
                if possibility in self.valeurs_lignes_par_3[0] and possibility in self.valeurs_lignes_par_3[1]:
                    if self.position in self.positions_colonnes_par_3[0]:
                        if possibility in self.valeurs_colonnes_par_3[1] and possibility in self.valeurs_colonnes_par_3[2]:
                            jeu.grille_updated[self.numero_ligne][self.numero_colonne].valeur = possibility
                    elif self.position in self.positions_colonnes_par_3[1]:
                        if possibility in self.valeurs_colonnes_par_3[0] and possibility in self.valeurs_colonnes_par_3[2]:
                            jeu.grille_updated[self.numero_ligne][self.numero_colonne].valeur = possibility
                    elif self.position in self.positions_colonnes_par_3[2]:
                        if possibility in self.valeurs_colonnes_par_3[0] and possibility in self.valeurs_colonnes_par_3[1]:
                            jeu.grille_updated[self.numero_ligne][self.numero_colonne].valeur = possibility

    def third_verification(self, jeu):
        total_possibilities = []
        for cellule in sum(jeu.grille_updated, []):
#            print(f"cellule testée : {cellule.position} || valeur : {cellule.valeur}")  # ----------------------------------------------------------------------------
            if cellule.position != self.position and cellule.position in self.positions_square_appartenance and cellule.valeur == " ":
                total_possibilities.append(cellule.possibilities)
                print(f"Cellule : {cellule.position} || Possibilities : {cellule.possibilities}")  # ----------------------------------------------------------------------------
        total_possibilities = sorted(list(set(sum(total_possibilities, []))))
        for possibility in self.possibilities:
            if not possibility in total_possibilities:
                jeu.grille_updated[self.numero_ligne][self.numero_colonne].valeur = possibility
#        print(total_possibilities)  # ----------------------------------------------------------------------------

        total_possibilities = []
        for cellule in sum(jeu.grille_updated, []):
            if cellule.position != self.position and cellule.position in self.positions_ligne_appartenance and cellule.valeur == " ":
                total_possibilities.append(cellule.possibilities)
#                print(f"Cellule : {cellule.position} || Possibilities : {cellule.possibilities}")  # ----------------------------------------------------------------------------
        total_possibilities = sorted(list(set(sum(total_possibilities, []))))
        for possibility in self.possibilities:
            if not possibility in total_possibilities:
                jeu.grille_updated[self.numero_ligne][self.numero_colonne].valeur = possibility
#        print(total_possibilities)  # ----------------------------------------------------------------------------

        total_possibilities = []
        for cellule in sum(jeu.grille_updated, []):
            if cellule.position != self.position and cellule.position in self.positions_colonne_appartenance and cellule.valeur == " ":
#                print(f"colonne appartenance : {self.positions_colonne_appartenance}")  # ----------------------------------------------------------------------------
                total_possibilities.append(cellule.possibilities)
#                print(f"Cellule : {cellule.position} || Possibilities : {cellule.possibilities}")  # ----------------------------------------------------------------------------
        total_possibilities = sorted(list(set(sum(total_possibilities, []))))
        for possibility in self.possibilities:
            if not possibility in total_possibilities:
                jeu.grille_updated[self.numero_ligne][self.numero_colonne].valeur = possibility
#        print(total_possibilities)  # ----------------------------------------------------------------------------

