import pygame

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
LARGEUR, HAUTEUR = 600, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Déplace le carré !")

# Couleurs
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)

# Propriétés du carré
carre_taille = 50
carre_x = LARGEUR // 2 - carre_taille // 2  # Position initiale (centre)
carre_y = HAUTEUR // 2 - carre_taille // 2
vitesse = 5  # Vitesse de déplacement

# Boucle principale
jeu_actif = True
clock = pygame.time.Clock()

while jeu_actif:
    pygame.time.delay(10)  # Petite pause pour limiter la vitesse

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu_actif = False

    # Détection des touches
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and carre_x > 0:
        carre_x -= vitesse
    if touches[pygame.K_RIGHT] and carre_x < LARGEUR - carre_taille:
        carre_x += vitesse
    if touches[pygame.K_UP] and carre_y > 0:
        carre_y -= vitesse
    if touches[pygame.K_DOWN] and carre_y < HAUTEUR - carre_taille:
        carre_y += vitesse

    # Dessin
    fenetre.fill(BLANC)  # Efface l'écran
    pygame.draw.rect(fenetre, ROUGE, (carre_x, carre_y, carre_taille, carre_taille))  # Dessine le carré

    # Mettre à jour l'affichage
    pygame.display.update()
    clock.tick(30)  # Limite à 30 FPS

# Quitter Pygame
pygame.quit()
