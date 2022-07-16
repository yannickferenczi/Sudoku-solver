class Grille:
    def __init__(self):
        self.cellules_organisees = [
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

        self.positions_cellules = []
        for ligne in range(9):
            positions_cellules_dans_ligne = []
            for colonne in range(9):
                position_cellule = (str(ligne), str(colonne))
                positions_cellules_dans_ligne.append(position_cellule)
            self.positions_cellules.append(positions_cellules_dans_ligne)

        self.infos_cellules = {}
        for cellule in sum(self.positions_cellules, []):
#            print(cellule)  # ----------------------------------------------------------------------------
            self.infos_cellules[cellule] = Cellule(self.cellules_organisees, self.positions_cellules, int(cellule[0]), int(cellule[1]))
        
    def display(self):
        for row in self.cellules_organisees:
            print(f"| {' | '.join(row[i] for i in range(9))} |")
            print("-"*37)

"""
class Ligne_par_3:
    def __init__(self, jeu, numero_lignes):
        self.liste_valeurs_cellules = sum([jeu.cellules_organisees[i] for i in numero_lignes], [])
        self.valeurs_ligne_haute = jeu.cellules_organisees[numero_lignes[0]]
        self.valeurs_ligne_milieu = jeu.cellules_organisees[numero_lignes[1]]
        self.valeurs_ligne_basse = jeu.cellules_organisees[numero_lignes[2]]

        self.liste_positions_cellules = sum([jeu.positions_cellules[i] for i in numero_lignes[0:3]], [])
        self.positions_ligne_haute = jeu.positions_cellules[numero_lignes[0]]
        self.positions_ligne_milieu = jeu.positions_cellules[numero_lignes[1]]
        self.positions_ligne_basse = jeu.positions_cellules[numero_lignes[2]]

class Colonne_par_3:
    def __init__(self, jeu, numero_colonnes):
        self.liste_valeurs_cellules = sum([jeu.cellules_organisees[i][(numero_colonnes[0:3])] for i in range(9)], [])
        self.valeurs_colonne_left = sum([jeu.cellules_organisees[i][numero_colonnes[0]] for i in range(9)], [])
        self.valeurs_colonne_milieu = sum([jeu.cellules_organisees[i][numero_colonnes[1]] for i in range(9)], [])
        self.valeurs_colonne_right = sum([jeu.cellules_organisees[i][numero_colonnes[2]] for i in range(9)], [])

        self.liste_positions_cellules = sum([jeu.positions_cellules[i][(numero_colonnes[0:3])] for i in range(9)], [])
        self.positions_colonne_left = sum([jeu.positions_cellules[i][numero_colonnes[0]] for i in range(9)], [])
        self.positions_colonne_milieu = sum([jeu.positions_cellules[i][numero_colonnes[1]] for i in range(9)], [])
        self.positions_colonne_right = sum([jeu.positions_cellules[i][numero_colonnes[2]] for i in range(9)], [])
"""

class Cellule:
    def __init__(self, cellules_organisees, positions_cellules, numero_ligne, numero_colonne):
        self.position = (str(numero_ligne), str(numero_colonne))
        self.numero_ligne = numero_ligne
        self.numero_colonne = numero_colonne
        self.possibilities = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.valeur = cellules_organisees[self.numero_ligne][self.numero_colonne]
        self.valeurs_ligne_appartenance = cellules_organisees[self.numero_ligne]
        self.positions_ligne_appartenance = cellules_organisees[self.numero_ligne]
        self.valeurs_colonne_appartenance = [cellules_organisees[i][self.numero_colonne] for i in range(9)]
        self.positions_colonne_appartenance = [positions_cellules[i][self.numero_colonne] for i in range(9)]
        self.positions_square_appartenance, self.positions_lignes_par_3, self.positions_colonnes_par_3 = self.determine_positions_square_lignes_par_3_colonnes_par_trois(positions_cellules)
        self.valeurs_square_appartenance, self.valeurs_lignes_par_3, self.valeurs_colonnes_par_3 = self.determine_valeurs_square_lignes_par_3_colonnes_par_trois(cellules_organisees)

    def update_valeurs(self, cellules_organisees):
        self.valeur = cellules_organisees[self.numero_ligne][self.numero_colonne]
        self.valeurs_ligne_appartenance = cellules_organisees[self.numero_ligne]
        self.valeurs_colonne_appartenance = [cellules_organisees[i][self.numero_colonne] for i in range(9)]
        self.valeurs_square_appartenance, self.valeurs_lignes_par_3, self.valeurs_colonnes_par_3 = self.determine_valeurs_square_lignes_par_3_colonnes_par_trois(cellules_organisees)


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
    
    def determine_valeurs_square_lignes_par_3_colonnes_par_trois(self, cellules_organisees):
        if self.numero_ligne <= 2:
            valeurs_lignes_par_3 = [cellules_organisees[i] for i in range(3)]
            if self.numero_colonne <= 2:
                valeurs_square = sum([cellules_organisees[i][:3] for i in range(3)], [])
                valeurs_colonnes_par_3 = [cellules_organisees[i][:3] for i in range(9)]
            elif 3 <= self.numero_colonne <= 5:
                valeurs_square = sum([cellules_organisees[i][3:6] for i in range(3)], [])
                valeurs_colonnes_par_3 = [cellules_organisees[i][3:6] for i in range(9)]
            elif 6 <= self.numero_colonne:
                valeurs_square = sum([cellules_organisees[i][6:9] for i in range(3)], [])
                valeurs_colonnes_par_3 = [cellules_organisees[i][6:9] for i in range(9)]
        elif 3 <= self.numero_ligne <= 5:
            valeurs_lignes_par_3 = [cellules_organisees[i] for i in range(3, 6)]
            if self.numero_colonne <= 2:
                valeurs_square = sum([cellules_organisees[i][:3] for i in range(3, 6)], [])
                valeurs_colonnes_par_3 = [cellules_organisees[i][:3] for i in range(9)]
            elif 3 <= self.numero_colonne <= 5:
                valeurs_square = sum([cellules_organisees[i][3:6] for i in range(3, 6)], [])
                valeurs_colonnes_par_3 = [cellules_organisees[i][3:6] for i in range(9)]
            elif 6 <= self.numero_colonne:
                valeurs_square = sum([cellules_organisees[i][6:9] for i in range(3, 6)], [])
                valeurs_colonnes_par_3 = [cellules_organisees[i][6:9] for i in range(9)]
        elif 6 <= self.numero_ligne:
            valeurs_lignes_par_3 = [cellules_organisees[i] for i in range(6, 9)]
            if self.numero_colonne <= 2:
                valeurs_square = sum([cellules_organisees[i][:3] for i in range(6, 9)], [])
                valeurs_colonnes_par_3 = [cellules_organisees[i][:3] for i in range(9)]
            elif 3 <= self.numero_colonne <= 5:
                valeurs_square = sum([cellules_organisees[i][3:6] for i in range(6, 9)], [])
                valeurs_colonnes_par_3 = [cellules_organisees[i][3:6] for i in range(9)]
            elif 6 <= self.numero_colonne:
                valeurs_square = sum([cellules_organisees[i][6:9] for i in range(6, 9)], [])
                valeurs_colonnes_par_3 = [cellules_organisees[i][6:9] for i in range(9)]
        return valeurs_square, valeurs_lignes_par_3, valeurs_colonnes_par_3
    
    def first_verification(self, jeu):
        not_possible = []
        for possibility in self.possibilities:
            if possibility in self.valeurs_ligne_appartenance or possibility in self.valeurs_colonne_appartenance or possibility in self.valeurs_square_appartenance:
                not_possible.append(possibility)
        for solution in not_possible:
            self.possibilities.remove(solution)
        if len(self.possibilities) == 1 and self.valeur == " ":
            jeu.cellules_organisees[self.numero_ligne][self.numero_colonne] = self.possibilities[0]

    def second_verification(self, jeu):
        if self.position in self.positions_lignes_par_3[0]:
            for possibility in self.possibilities:
                if possibility in self.valeurs_lignes_par_3[1] and possibility in self.valeurs_lignes_par_3[2]:
                    if self.position in self.positions_colonnes_par_3[0]:
                        if possibility in self.valeurs_colonnes_par_3[1] and possibility in self.valeurs_colonnes_par_3[2]:
                            jeu.cellules_organisees[self.numero_ligne][self.numero_colonne] = possibility
                    elif self.position in self.positions_colonnes_par_3[1]:
                        if possibility in self.valeurs_colonnes_par_3[0] and possibility in self.valeurs_colonnes_par_3[2]:
                            jeu.cellules_organisees[self.numero_ligne][self.numero_colonne] = possibility
                    elif self.position in self.positions_colonnes_par_3[2]:
                        if possibility in self.valeurs_colonnes_par_3[0] and possibility in self.valeurs_colonnes_par_3[1]:
                            jeu.cellules_organisees[self.numero_ligne][self.numero_colonne] = possibility
        elif self.position in self.positions_lignes_par_3[1]:
            for possibility in self.possibilities:
                if possibility in self.valeurs_lignes_par_3[0] and possibility in self.valeurs_lignes_par_3[2]:
                    if self.position in self.positions_colonnes_par_3[0]:
                        if possibility in self.valeurs_colonnes_par_3[1] and possibility in self.valeurs_colonnes_par_3[2]:
                            jeu.cellules_organisees[self.numero_ligne][self.numero_colonne] = possibility
                    elif self.position in self.positions_colonnes_par_3[1]:
                        if possibility in self.valeurs_colonnes_par_3[0] and possibility in self.valeurs_colonnes_par_3[2]:
                            jeu.cellules_organisees[self.numero_ligne][self.numero_colonne] = possibility
                    elif self.position in self.positions_colonnes_par_3[2]:
                        if possibility in self.valeurs_colonnes_par_3[0] and possibility in self.valeurs_colonnes_par_3[1]:
                            jeu.cellules_organisees[self.numero_ligne][self.numero_colonne] = possibility
        elif self.position in self.positions_lignes_par_3[2]:
            for possibility in self.possibilities:
                if possibility in self.valeurs_lignes_par_3[0] and possibility in self.valeurs_lignes_par_3[1]:
                    if self.position in self.positions_colonnes_par_3[0]:
                        if possibility in self.valeurs_colonnes_par_3[1] and possibility in self.valeurs_colonnes_par_3[2]:
                            jeu.cellules_organisees[self.numero_ligne][self.numero_colonne] = possibility
                    elif self.position in self.positions_colonnes_par_3[1]:
                        if possibility in self.valeurs_colonnes_par_3[0] and possibility in self.valeurs_colonnes_par_3[2]:
                            jeu.cellules_organisees[self.numero_ligne][self.numero_colonne] = possibility
                    elif self.position in self.positions_colonnes_par_3[2]:
                        if possibility in self.valeurs_colonnes_par_3[0] and possibility in self.valeurs_colonnes_par_3[1]:
                            jeu.cellules_organisees[self.numero_ligne][self.numero_colonne] = possibility

    def third_verification(self, jeu):
        total_possibilities = []
        for cellule in jeu.infos_cellules.values():
            print(f"cellule testée : {cellule.position} || valeur : {cellule.valeur}")  # ----------------------------------------------------------------------------
            if cellule.position != self.position and cellule.position in self.positions_square_appartenance and cellule.valeur == " ":
                total_possibilities.append(cellule.possibilities)
                print(f"Cellule : {cellule.position} || Possibilities : {cellule.possibilities}")
        total_possibilities = sorted(list(set(sum(total_possibilities, []))))
        for possibility in self.possibilities:
            if not possibility in total_possibilities:
                jeu.cellules_organisees[self.numero_ligne][self.numero_colonne] = possibility
        print(total_possibilities)  # ----------------------------------------------------------------------------

        total_possibilities = []
        for cellule in jeu.infos_cellules.values():
            if cellule.position != self.position and cellule.position in self.positions_ligne_appartenance and cellule.valeur == " ":
                total_possibilities.append(cellule.possibilities)
#                print(f"Cellule : {cellule.position} || Possibilities : {cellule.possibilities}")  # ----------------------------------------------------------------------------
        total_possibilities = sorted(list(set(sum(total_possibilities, []))))
        for possibility in self.possibilities:
            if not possibility in total_possibilities:
                jeu.cellules_organisees[self.numero_ligne][self.numero_colonne] = possibility
        print(total_possibilities)  # ----------------------------------------------------------------------------

        total_possibilities = []
        for cellule in jeu.infos_cellules.values():
            if cellule.position != self.position and cellule.position in self.positions_colonne_appartenance and cellule.valeur == " ":
#                print(f"colonne appartenance : {self.positions_colonne_appartenance}")  # ----------------------------------------------------------------------------
                total_possibilities.append(cellule.possibilities)
#                print(f"Cellule : {cellule.position} || Possibilities : {cellule.possibilities}")  # ----------------------------------------------------------------------------
        total_possibilities = sorted(list(set(sum(total_possibilities, []))))
        for possibility in self.possibilities:
            if not possibility in total_possibilities:
                jeu.cellules_organisees[self.numero_ligne][self.numero_colonne] = possibility
        print(total_possibilities)  # ----------------------------------------------------------------------------

