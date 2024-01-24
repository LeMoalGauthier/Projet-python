import pygame
import sys
from vector import Vector2
from constants import *
from map import Map

# Initialisation de Pygame
pygame.init()


# Créer la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Node Test")

# Création de la carte
map.instance = Map()

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacer l'écran
    screen.fill(BLACK)

    # Afficher les nœuds et leurs connexions
    for node in nodeList:
        node.render(screen)

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()