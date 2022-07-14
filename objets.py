class Grille:
    def __init__(self):
        self.cellules_organisees = [
            ["1", "2", "3", " ", " ", " ", " ", " ", " "],
            ["4", "5", "6", " ", "2", " ", " ", " ", " "],
            ["7", "8", " ", " ", " ", " ", " ", " ", "5"],
            [" ", " ", " ", " ", "5", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", "2", " ", " "],
            [" ", " ", "5", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", "5", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " ", "2"]
        ]

        self.positions_cellules = []
        for ligne in range(9):
            positions_cellules_dans_ligne = []
            for colonne in range(9):
                position_cellule = (str(ligne), str(colonne))
                positions_cellules_dans_ligne.append(position_cellule)
            self.positions_cellules.append(positions_cellules_dans_ligne)
        
    def display(self):
        for row in self.cellules_organisees:
            print(f"| {' | '.join(row[i] for i in range(9))} |")
            print("-"*37)


class Square:
    def __init__(self, jeu, numero_lignes, numero_colonne_gauche):
        self.liste_valeurs_cellules = sum([jeu.cellules_organisees[i][numero_colonne_gauche:numero_colonne_gauche + 3] for i in range(numero_lignes)], [])
        self.liste_positions_cellules = sum([jeu.positions_cellules[i][numero_colonne_gauche:numero_colonne_gauche + 3] for i in range(numero_lignes)], [])

class Ligne_par_3:
    def __init__(self, jeu, numero_lignes):
        self.liste_valeurs_cellules = sum([jeu.cellules_organisees[i] for i in range(numero_lignes)], [])
        self.valeurs_ligne_haute = jeu.cellules_organisees[numero_lignes[0]]
        self.valeurs_ligne_milieu = jeu.cellules_organisees[numero_lignes[1]]
        self.valeurs_ligne_basse = jeu.cellules_organisees[numero_lignes[2]]

        self.liste_positions_cellules = sum([jeu.positions_cellules[i] for i in range(numero_lignes)], [])
        self.positions_ligne_haute = jeu.positions_cellules[numero_lignes[0]]
        self.positions_ligne_milieu = jeu.positions_cellules[numero_lignes[1]]
        self.positions_ligne_basse = jeu.positions_cellules[numero_lignes[2]]

class Colonne_par_3:
    def __init__(self, jeu, numero_colonnes):
        self.liste_valeurs_cellules = sum([jeu.cellules_organisees[i][numero_colonnes] for i in range(9)], [])
        self.valeurs_colonne_left = sum([jeu.cellules_organisees[i][numero_colonnes[0]] for i in range(9)], [])
        self.valeurs_colonne_milieu = sum([jeu.cellules_organisees[i][numero_colonnes[1]] for i in range(9)], [])
        self.valeurs_colonne_right = sum([jeu.cellules_organisees[i][numero_colonnes[2]] for i in range(9)], [])

        self.liste_positions_cellules = sum([jeu.positions_cellules[i][numero_colonnes] for i in range(9)], [])
        self.positions_colonne_left = sum([jeu.positions_cellules[i][numero_colonnes[0]] for i in range(9)], [])
        self.positions_colonne_milieu = sum([jeu.positions_cellules[i][numero_colonnes[1]] for i in range(9)], [])
        self.positions_colonne_right = sum([jeu.positions_cellules[i][numero_colonnes[2]] for i in range(9)], [])

class Cellule:
    def __init__(self, jeu, numero_ligne, numero_colonne):
        self.position = (numero_ligne, numero_colonne)
        self.numero_ligne = numero_ligne
        self.numero_colonne = numero_colonne
        self.possibilities = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.valeur = jeu.cellules_organisees[self.numero_ligne][self.numero_colonne]
        self.ligne_appartenance = jeu.cellules_organisees[self.numero_ligne]
        self.colonne_appartenance = [jeu.cellules_organisees[i][self.numero_colonne] for i in range(9)]
        if self.numero_ligne <= 2:
            if self.numero_colonne <= 2:
                self.square_appartenance = sum([jeu.cellules_organisees[i][:3] for i in range(3)], [])  # "S1"
            elif 3 <= self.numero_colonne <= 5:
                self.square_appartenance = sum([jeu.cellules_organisees[i][3:6] for i in range(3)], [])  # "S2"
            elif 6 <= self.numero_colonne:
                self.square_appartenance = sum([jeu.cellules_organisees[i][6:9] for i in range(3)], [])  # "S3"
        elif 3 <= self.numero_ligne <= 5:
            if self.numero_colonne <= 2:
                self.square_appartenance = sum([jeu.cellules_organisees[i][:3] for i in range(3, 6)], [])  # "S4"
            elif 3 <= self.numero_colonne <= 5:
                self.square_appartenance = sum([jeu.cellules_organisees[i][3:6] for i in range(3, 6)], [])  # "S5"
            elif 6 <= self.numero_colonne:
                self.square_appartenance = sum([jeu.cellules_organisees[i][6:9] for i in range(3, 6)], [])  # "S6"
        elif 6 <= self.numero_ligne:
            if numero_colonne <= 2:
                self.square_appartenance = sum([jeu.cellules_organisees[i][:3] for i in range(6, 9)], [])  # "S7"
            elif 3 <= self.numero_colonne <= 5:
                self.square_appartenance = sum([jeu.cellules_organisees[i][3:6] for i in range(6, 9)], [])  # "S8"
            elif 6 <= self.numero_colonne:
                self.square_appartenance = sum([jeu.cellules_organisees[i][6:9] for i in range(6, 9)], [])  # "S9"
    

    def verification(self, jeu):
        for possibility in self.possibilities:
            if possibility in self.ligne_appartenance or possibility in self.colonne_appartenance or possibility in self.square_appartenance:
                self.possibilities.remove(possibility)
        print(self.possibilities)
        if len(self.possibilities) == 1 and self.valeur == " ":
            jeu.cellules_organisees[self.numero_ligne][self.numero_colonne] = self.possibilities[0]
            self.valeur = self.possibilities[0]
