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

def out_of_screen (vitesse_personnage, direction):
    if perso_pacman.x < 0:
        direction = 'right'
        perso_pacman.deplacer(vitesse_personnage, direction)
    if perso_pacman.x > 950:
        direction = 'left'
        perso_pacman.deplacer(vitesse_personnage, direction)
    if perso_pacman.y < 0:
        direction = 'down'
        perso_pacman.deplacer(vitesse_personnage, direction)
    if perso_pacman.y > 550:
        direction = 'up'
        perso_pacman.deplacer(vitesse_personnage, direction)
    return direction

pygame.init()
ecran = pygame.display.set_mode((1000, 600))
perso_pacman = Move.Personnage(10, 50, "Pacman_perso.png")
perso_pacman_full = Move.Personnage(10, 50, "Pacman_perso_full.png")
vitesse_personnage = 5

direction = ""
index_eat = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Pour fermer la fenetre du jeu
            pygame.quit()
            sys.exit()

    new_direction = check_keyboard_presses()

    if new_direction:
        direction = new_direction


    perso_pacman.deplacer(vitesse_personnage, direction)
    direction = out_of_screen(vitesse_personnage, direction)
    ecran.fill((0, 0, 0))

    if index_eat %4 ==0:
        ecran.blit(perso_pacman_full.image, (perso_pacman.x, perso_pacman.y))
    else:
        ecran.blit(perso_pacman.image, (perso_pacman.x, perso_pacman.y))
    index_eat+=1

    pygame.display.flip()
    pygame.time.Clock().tick(30)
