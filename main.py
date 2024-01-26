import pygame
import sys
import platform

import Move


_OS = platform.system()   # Détecte le système d'exploitation
if _OS == "Windows":
    import win32api
elif _OS == "Darwin":
    from Quartz import CGEventSourceButtonState, kCGEventSourceStateHIDSystemState, kCGMouseButtonLeft

def check_keyboard_presses():
    # Vérifie si une touche est enfoncée et renvoyer la direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        return "right"
    elif keys[pygame.K_LEFT]:
        return "left"
    elif keys[pygame.K_UP]:
        return "up"
    elif keys[pygame.K_DOWN]:
        return "down"
    else:
        return ""

pygame.init()
ecran = pygame.display.set_mode((1000, 600))
perso_pacman = Move.Personnage(10, 50, "Pacman_perso.png")
vitesse_personnage = 5

direction = ""

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Pour fermer la fenetre du jeu
            pygame.quit()
            sys.exit()

    new_direction = check_keyboard_presses()

    if new_direction:
        direction = new_direction

    perso_pacman.deplacer(vitesse_personnage, direction)

    ecran.fill((0, 0, 0))
    ecran.blit(perso_pacman.image, (perso_pacman.x, perso_pacman.y))

    pygame.display.flip()
    pygame.time.Clock().tick(30)
