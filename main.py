import pygame
import platform
import constants
import sys
from nodes import NodeGroup

_OS = platform.system()
if _OS == "Windows":
    import win32api
elif _OS == "Darwin":
    from Quartz import CGEventSourceButtonState, kCGEventSourceStateHIDSystemState, kCGMouseButtonLeft


if __name__ == '__main__':

    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Map Test")

    # Chemin vers le fichier de texte du labyrinthe
    maze_file_path = "carte1.txt"

    # Créer une instance de la classe NodeGroup
    node_group = NodeGroup(maze_file_path)

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Effacer l'écran
        screen.fill(constants.BACKGROUND_COLOR)  # Remplacez la couleur blanche par celle de votre choix

        # Mettre à jour l'affichage
        pygame.display.flip()

    # Quitter Pygame
    pygame.quit()
    sys.exit()
