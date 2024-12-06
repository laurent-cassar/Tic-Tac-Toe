# Fonction pour afficher le tableau de jeu
def afficher_grille(grille):
    for i in range(3):
        print(" | ".join(grille[i]))
        if i < 2:
            print("---------")

# Fonction pour vérifier si un joueur a gagné
def verifier_victoire(grille, joueur):
    # Vérification des lignes
    for i in range(3):
        if grille[i][0] == grille[i][1] == grille[i][2] == joueur:
            return True
    # Vérification des colonnes
    for i in range(3):
        if grille[0][i] == grille[1][i] == grille[2][i] == joueur:
            return True
    # Vérification des diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] == joueur:
        return True
    if grille[0][2] == grille[1][1] == grille[2][0] == joueur:
        return True
    return False

# Fonction pour vérifier si la grille est pleine
def grille_pleine(grille):
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                return False
    return True

# Fonction principale du jeu
def morpion():
    grille = [[" " for _ in range(3)] for _ in range(3)]
    joueurs = ["X", "O"]
    tour = 0
    
    while True:
        afficher_grille(grille)
        joueur_courant = joueurs[tour % 2]
        print(f"Au tour de {joueur_courant}")
        
        # Demander la position du mouvement
        try:
            ligne = int(input("Entrez le numéro de la ligne (0, 1, 2) : "))
            colonne = int(input("Entrez le numéro de la colonne (0, 1, 2) : "))
            
            if grille[ligne][colonne] != " ":
                print("Cette case est déjà occupée, essayez encore.")
                continue
        except (ValueError, IndexError):
            print("Entrée invalide, réessayez.")
            continue
        
        # Placer le symbole du joueur sur la grille
        grille[ligne][colonne] = joueur_courant
        
        # Vérification de la victoire
        if verifier_victoire(grille, joueur_courant):
            afficher_grille(grille)
            print(f"Le joueur {joueur_courant} a gagné!")
            break
        
        # Vérification de match nul
        if grille_pleine(grille):
            afficher_grille(grille)
            print("C'est un match nul!")
            break
        
        # Passer au tour suivant
        tour += 1

# Lancer le jeu
if __name__ == "__main__":
    morpion()
