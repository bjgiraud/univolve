import random

# Définition des constantes
TAILLE_GRILLE = 8
POPULATION_INITIALE = 5
POPULATION_MAX_PAR_ESPECE = 100
CHANCE_MUTATION = 0.1

class Espece:
    def __init__(self, nom, population):
        self.nom = nom
        self.population = population

    def se_reproduire(self):
        if self.population < POPULATION_MAX_PAR_ESPECE:
            self.population += random.randint(1, 10)
            return True
        return False

    def mourir(self):
        if self.population > 0:
            self.population -= random.randint(1, 5)

class Case:
    def __init__(self):
        self.espece = None

    def coloniser(self, espece):
        if self.espece is None:
            self.espece = espece

    def evacuer(self):
        self.espece = None

def afficher_grille(grille):
    for ligne in grille:
        for case in ligne:
            if case.espece:
                #print(f"{case.espece.nom}{case.espece.population}", end="\t")
                print(f"{case.espece.nom}", end="\t")
            else:
                print("-", end="\t")
        print()

def simulation():
    # Initialisation de la grille
    grille = [[Case() for _ in range(TAILLE_GRILLE)] for _ in range(TAILLE_GRILLE)]

    # Placement des premières espèces
    #especes = ["▣", "◼", "◩", "◢", "◫", "◎", "◮", "◿", "★","⚈"]  # Ajoutez plus d'espèces au besoin
    #especes = ["♔","♕","♖","♗","♘","♙","♚","♛","♜","♝","♞","♟","♠","♡","♢","♣","♤","♥","♦","♧"]  # Ajoutez plus d'espèces au besoin
    especes = ["ぁ","あ","ぃ","い","ぅ","う","ぇ","え","ぉ","お","か","が","き","ぎ","く","ぐ","け","げ","こ","ご","さ","ざ","し","じ","す","ず","せ","ぜ","そ","ぞ","た","だ","ち","ぢ","っ","つ","づ","て","で","と","ど","な","に","ぬ","ね","の","は","ば","ぱ","ひ","び","ぴ","ふ","ぶ","ぷ","へ","べ","ぺ","ほ","ぼ","ぽ","ま","み","む","め","も","ゃ","や","ゅ","ゆ","ょ","よ","ら","り","る","れ","ろ","ゎ","わ","ゐ","ゑ","を","ん","ゔ","ゕ","ゖ"]  # Ajoutez plus d'espèces au besoin
    for _ in range(POPULATION_INITIALE):
        x, y = random.randint(0, TAILLE_GRILLE-1), random.randint(0, TAILLE_GRILLE-1)
        espece = Espece(random.choice(especes), random.randint(1, POPULATION_MAX_PAR_ESPECE))
        grille[x][y].coloniser(espece)

    # Simulation
    for _ in range(100):
        for i in range(TAILLE_GRILLE):
            for j in range(TAILLE_GRILLE):
                case = grille[i][j]
                if case.espece:
                    if case.espece.se_reproduire():
                        # Check for mutation
                        if random.random() < CHANCE_MUTATION:
                            new_population = random.randint(1, POPULATION_MAX_PAR_ESPECE)
                            new_espece = Espece(case.espece.nom, new_population)
                            case.coloniser(new_espece)
                    case.espece.mourir()

                    # Déplacement des espèces si la capacité est dépassée
                    if case.espece.population > POPULATION_MAX_PAR_ESPECE:
                        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                        random.shuffle(directions)
                        for dx, dy in directions:
                            new_x, new_y = i + dx, j + dy
                            if 0 <= new_x < TAILLE_GRILLE and 0 <= new_y < TAILLE_GRILLE:
                                if not grille[new_x][new_y].espece:
                                    nouvelle_colonie = Espece(case.espece.nom, case.espece.population // 2)
                                    case.espece.population //= 2
                                    grille[new_x][new_y].coloniser(nouvelle_colonie)
                                    break

        # Affichage de la grille à chaque itération
        print("Tour :", _)
        afficher_grille(grille)
        print()

if __name__ == "__main__":
    simulation()
