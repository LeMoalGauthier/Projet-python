import pygame
import sys


class Personnage:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.image_right = pygame.image.load(image_path).convert_alpha()
        self.image_right = pygame.transform.scale(self.image_right, (60, 50))
        self.image_left = pygame.transform.flip(self.image_right, True, False)  # Image miroir
        self.image = self.image_right  # Image par défaut (vers la droite)

    def deplacer(self, vitesse, direction):
        if direction == "right":
            self.image = self.image_right
            self.x += vitesse
        elif direction == "left":
            self.image = self.image_left  # Utilise l'image miroir
            self.x -= vitesse
        elif direction == "up":
            self.y -= vitesse
        elif direction == "down":
            self.y += vitesse
