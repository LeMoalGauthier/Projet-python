import pygame
from vector import Vector2
from constants import *
import numpy as np


class Food(object):
    def __init__(self, row, column):
        self.name = Food
        self.position = Vector2(column * TILEWIDTH, row * TILEHEIGHT)
        self.color = WHITE
        self.radius = int(2 * TILEWIDTH / 16)
        self.collideRadius = 2 * TILEWIDTH / 16
        self.points = 10
        self.visible = True

    def render(self, screen):
        if self.visible:
            adjust = Vector2(TILEWIDTH, TILEHEIGHT) / 2
            p = self.position + adjust
            pygame.draw.circle(screen, self.color, p.asInt(), self.radius)


class Powerfood(Food):
    def __init__(self, row, column):
        Food.__init__(self, row, column)
        self.name = POWERFOOD
        self.radius = int(8 * TILEWIDTH / 16)
        self.points = 50
        self.flashTime = 0.2
        self.timer = 0

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.flashTime:
            self.visible = not self.visible
            self.timer = 0


class foodGroup(object):
    def __init__(self, foodfile):
        self.foodList = []
        self.powerfood = []
        self.createfoodList(foodfile)
        self.numEaten = 0

    def update(self, dt):
        for powerfood in self.powerfood:
            powerfood.update(dt)

    def createfoodList(self, foodfile):
        data = self.readfoodfile(foodfile)
        for row in range(data.shape[0]):
            for col in range(data.shape[1]):
                if data[row][col] in ['.', '+']:
                    self.foodList.append(Food(row, col))
                elif data[row][col] in ['P', 'p']:
                    pp = Powerfood(row, col)
                    self.foodList.append(pp)
                    self.powerfood.append(pp)

    def readfoodfile(self, textfile):
        return np.loadtxt(textfile, dtype='<U1')

    def isEmpty(self):
        if len(self.foodList) == 0:
            return True
        return False

    def render(self, screen):
        for food in self.foodList:
            food.render(screen)