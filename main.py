import pygame
import sys
import platform
import random

# modes.py

SCATTER = 0
CHASE = 1
FLEE = 2
SPAWN = 3

class ModeController:
    def __init__(self):
        self.current_mode = SCATTER  # Démarre en mode Scatter
        self.mode_duration = 7  # Durée du mode Scatter en secondes
        self.chase_duration = 20  # Durée du mode Chase en secondes
        self.timer = 0  # Timer pour suivre la durée des modes

    def switch_mode(self):
        if self.current_mode == SCATTER:
            self.current_mode = CHASE
            self.timer = self.chase_duration
        elif self.current_mode == CHASE:
            self.current_mode = SCATTER
            self.timer = self.mode_duration

    def update_timer(self, dt):
        self.timer -= dt
        if self.timer <= 0:
            self.switch_mode()

    def get_current_mode(self):
        return self.current_mode


#Move.py
import pygame
import sys
import platform
import random


class Personnage:
    def __init__(self, x, y, direction, image_path):
        self.x = x
        self.y = y
        self.direction = direction
        self.image_right = pygame.image.load(image_path).convert_alpha()
        self.image_right = pygame.transform.scale(self.image_right, (60, 50))
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right

    def deplacer(self, vitesse, direction):
        if direction == "right":
            self.image = self.image_right
            self.x += vitesse
        elif direction == "left":
            self.image = self.image_left
            self.x -= vitesse
        elif direction == "up":
            self.y -= vitesse
        elif direction == "down":
            self.y += vitesse


def check_keyboard_presses():
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


def out_of_screen(vitesse_personnage, direction, personnage):
    if personnage.x < 0:
        direction = 'right'
        personnage.deplacer(vitesse_personnage, direction)
    if personnage.x > 950:
        direction = 'left'
        personnage.deplacer(vitesse_personnage, direction)
    if personnage.y < 0:
        direction = 'down'
        personnage.deplacer(vitesse_personnage, direction)
    if personnage.y > 550:
        direction = 'up'
        personnage.deplacer(vitesse_personnage, direction)
    return direction


def move_randomly(pink_ghost, probability=0.1):
    rand = random.random()
    if rand < probability:
        directions = ['up', 'down', 'left', 'right']
        new_direction = random.choice(directions)
        pink_ghost.direction = new_direction


pygame.init()
ecran = pygame.display.set_mode((1000, 600))
perso_pacman = Personnage(10, 50, "", "Pacman_perso.png")
perso_pacman_full = Personnage(10, 50, "", "Pacman_perso_full.png")
pink_ghost = Personnage(300, 300, "", "pink_ghost.png")
orange_ghost = Personnage(300, 300, "", "orange_ghost.png")
red_ghost = Personnage(300, 300, "", "red_ghost.png")
blue_ghost = Personnage(300, 300, "", "blue_ghost.png")

vitesse_personnage = 5
index_eat = 0
mode_controller = ModeController()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    new_direction = check_keyboard_presses()

    if new_direction:
        perso_pacman.direction = new_direction

    move_randomly(pink_ghost)
    move_randomly(orange_ghost)
    move_randomly(blue_ghost)
    move_randomly(red_ghost)

    perso_pacman.deplacer(vitesse_personnage, perso_pacman.direction)

    if mode_controller.get_current_mode() == CHASE:
        # Le fantôme rose suit le mode CHASE
        # Ici, nous pourrions ajouter la logique pour que le fantôme rose suive le pacman
        pass
    elif mode_controller.get_current_mode() == SCATTER:
        # Le fantôme rose suit le mode SCATTER
        # Ici, nous pourrions ajouter la logique pour que le fantôme rose se dirige vers le coin supérieur gauche de l'écran
        pass

    pink_ghost.deplacer(vitesse_personnage, pink_ghost.direction)
    orange_ghost.deplacer(vitesse_personnage, orange_ghost.direction)
    red_ghost.deplacer(vitesse_personnage, red_ghost.direction)
    blue_ghost.deplacer(vitesse_personnage, blue_ghost.direction)

    perso_pacman.direction = out_of_screen(vitesse_personnage, perso_pacman.direction, perso_pacman)
    pink_ghost.direction = out_of_screen(vitesse_personnage, pink_ghost.direction, pink_ghost)
    orange_ghost.direction = out_of_screen(vitesse_personnage, orange_ghost.direction, orange_ghost)
    red_ghost.direction = out_of_screen(vitesse_personnage, red_ghost.direction, red_ghost)
    blue_ghost.direction = out_of_screen(vitesse_personnage, blue_ghost.direction, blue_ghost)

    ecran.fill((0, 0, 0))

    if index_eat % 4 == 0:
        ecran.blit(perso_pacman_full.image, (perso_pacman.x, perso_pacman.y))
    else:
        ecran.blit(perso_pacman.image, (perso_pacman.x, perso_pacman.y))
    index_eat += 1

    ecran.blit(pink_ghost.image, (pink_ghost.x, pink_ghost.y))
    ecran.blit(orange_ghost.image, (orange_ghost.x, orange_ghost.y))
    ecran.blit(red_ghost.image, (red_ghost.x, red_ghost.y))
    ecran.blit(blue_ghost.image, (blue_ghost.x, blue_ghost.y))

    pygame.display.flip()
    pygame.time.Clock().tick(30)
