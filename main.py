import pygame
import sys
import platform
import random

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

def out_of_screen (vitesse_personnage, direction, personnage):
    if  personnage.x < 0:
        direction = 'right'
        personnage.deplacer(vitesse_personnage, direction)
    if  personnage.x > 950:
        direction = 'left'
        personnage.deplacer(vitesse_personnage, direction)
    if  personnage.y < 0:
        direction = 'down'
        personnage.deplacer(vitesse_personnage, direction)
    if  personnage.y > 550:
        direction = 'up'
        personnage.deplacer(vitesse_personnage, direction)
    return direction

def move_randomly(pink_ghost, probability=0.1):
    # Génère un nombre aléatoire entre 0 et 1
    rand = random.random()
    # Si le nombre aléatoire est inférieur à la probabilité, change de direction
    if rand < probability:
        directions = ['up', 'down', 'left', 'right']
        new_direction = random.choice(directions)
        pink_ghost.direction = new_direction

pygame.init()
ecran = pygame.display.set_mode((1000, 600))
perso_pacman = Move.Personnage(10, 50, "","Pacman_perso.png")
perso_pacman_full = Move.Personnage(10, 50, "","Pacman_perso_full.png")
pink_ghost = Move.Personnage(300, 300, "","pink_ghost.png")
orange_ghost = Move.Personnage(300, 300, "","orange_ghost.png")
red_ghost = Move.Personnage(300, 300, "","red_ghost.png")
blue_ghost = Move.Personnage(300, 300, "","blue_ghost.png")

vitesse_personnage = 5


index_eat = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Pour fermer la fenetre du jeu
            pygame.quit()
            sys.exit()

    # On regarde si une touche a été pressée
    new_direction = check_keyboard_presses()

    if new_direction:
        perso_pacman.direction = new_direction # Attribution de la nouvelle position au PacMan

    # Déplacement aléatoire du fantôme rose

    move_randomly(pink_ghost)
    move_randomly(orange_ghost)
    move_randomly(blue_ghost)
    move_randomly(red_ghost)


    # Déplacement de l'abscisse et de l'ordonnée des personnages
    perso_pacman.deplacer(vitesse_personnage, perso_pacman.direction)
    pink_ghost.deplacer(vitesse_personnage, pink_ghost.direction)
    orange_ghost.deplacer(vitesse_personnage, orange_ghost.direction)
    red_ghost.deplacer(vitesse_personnage, red_ghost.direction)
    blue_ghost.deplacer(vitesse_personnage, blue_ghost.direction)



    #Vérification si le personnage est hors de l'écran

    perso_pacman.direction = out_of_screen(vitesse_personnage, perso_pacman.direction,perso_pacman)
    pink_ghost.direction = out_of_screen(vitesse_personnage, pink_ghost.direction,pink_ghost)
    orange_ghost.direction = out_of_screen(vitesse_personnage, orange_ghost.direction,orange_ghost)
    red_ghost.direction = out_of_screen(vitesse_personnage, red_ghost.direction,red_ghost)
    blue_ghost.direction = out_of_screen(vitesse_personnage, blue_ghost.direction,blue_ghost)

    ecran.fill((0, 0, 0))

    # Affichage de PacMan animé ( en ouvrant la bouche et en la fermant)
    if index_eat %4 ==0:
        ecran.blit(perso_pacman_full.image, (perso_pacman.x, perso_pacman.y))
    else:
        ecran.blit(perso_pacman.image, (perso_pacman.x, perso_pacman.y))
    index_eat+=1

    ecran.blit(pink_ghost.image, (pink_ghost.x, pink_ghost.y))
    ecran.blit(orange_ghost.image, (orange_ghost.x, orange_ghost.y))
    ecran.blit(red_ghost.image, (red_ghost.x, red_ghost.y))
    ecran.blit(blue_ghost.image, (blue_ghost.x, blue_ghost.y))

    # Affichage fenetre
    pygame.display.flip()
    pygame.time.Clock().tick(30)
