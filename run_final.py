import pygame
from pygame.locals import *
from constants import *
from pacman import Pacman
from nodes import NodeGroup
from food import foodGroup
from ghosts import GhostGroup
from text import TextGroup
from sprites import LifeSprites
from sprites import MazeSprites
from mazedata import MazeData


class Window(object):
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREENSIZE, 0, 32)
        self.background = None  # Initialise l'arrière-plan
        self.clock = pygame.time.Clock()  # Initialise l'horloge pour le framerate
        self.level = 0  # Initialise le niveau du jeu
        self.lives = 5  # Initialise le nombre de vies
        self.score = 0  # Initialise le score
        self.textgroup = TextGroup()  # Initialise le groupe de texte
        self.lifesprites = LifeSprites(self.lives)  # Initialise les sprites de vie
        self.mazedata = MazeData()  # Crée une instance de MazeData

    def setBackground(self):
        # Crée et initialise les surfaces pour l'arrière-plan
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)

    def startGame(self):
        self.mazedata.loadMaze(self.level)  # Charge le labyrinthe pour le niveau actuel
        self.mazesprites = MazeSprites(self.mazedata.obj.name + ".txt", self.mazedata.obj.name + "_rotation.txt")
        self.setBackground()  # Initialise l'arrière-plan
        self.background = self.mazesprites.constructBackground(self.background, self.level % 5)
        self.nodes = NodeGroup(self.mazedata.obj.name + ".txt")  # Initialise les nœuds du labyrinthe
        self.mazedata.obj.setPortalPairs(self.nodes)  # Configure les paires de portails
        self.mazedata.obj.connectHomeNodes(self.nodes)  # Connecte les nœuds de la maison
        self.pacman = Pacman(self.nodes.getNodeFromTiles(*self.mazedata.obj.pacmanStart))  # Initialise Pacman
        self.food = foodGroup(self.mazedata.obj.name + ".txt")  # Initialise les food
        self.ghosts = GhostGroup(self.nodes.getStartTempNode(), self.pacman)  # Initialise les fantômes

        # On attribue les positions de départ des fantômes

        self.ghosts.pinky.setStartNode(self.nodes.getNodeFromTiles(*self.mazedata.obj.addOffset(2, 3)))
        self.ghosts.inky.setStartNode(self.nodes.getNodeFromTiles(*self.mazedata.obj.addOffset(0, 3)))
        self.ghosts.clyde.setStartNode(self.nodes.getNodeFromTiles(*self.mazedata.obj.addOffset(4, 3)))
        self.ghosts.setSpawnNode(self.nodes.getNodeFromTiles(*self.mazedata.obj.addOffset(2, 3)))
        self.ghosts.blinky.setStartNode(self.nodes.getNodeFromTiles(*self.mazedata.obj.addOffset(2, 0)))

        # Configure les restrictions d'accès des nœuds de la maison pour Pacman et les fantômes
        self.nodes.denyHomeAccess(self.pacman)
        self.nodes.denyHomeAccessList(self.ghosts)
        self.ghosts.inky.startNode.denyAccess(RIGHT, self.ghosts.inky)
        self.ghosts.clyde.startNode.denyAccess(LEFT, self.ghosts.clyde)
        self.mazedata.obj.denyGhostsAccess(self.ghosts, self.nodes)

    def update(self):
        dt = self.clock.tick(30) / 1000.0  # Calcule le temps écoulé depuis la dernière mise à jour
        self.textgroup.update(dt)  # Met à jour le groupe de texte
        self.food.update(dt)  # Met à jour les food
        self.ghosts.update(dt)  # Met à jour les fantômes
        self.checkfoodEvents()  # Vérifie les événements liés aux food
        self.checkGhostEvents()  # Vérifie les événements liés aux fantômes

        if self.pacman.alive:
            self.pacman.update(dt)
        else:
            self.pacman.update(dt)

        self.checkEvents()  # Vérifie les événements de la fenêtre
        self.render()  # Affiche les éléments du jeu à l'écran

    def checkEvents(self):
        for event in pygame.event.get():  # Parcours des événements
            if event.type == QUIT:
                exit()  # Quitte le jeu

    def checkfoodEvents(self):
        food = self.pacman.eatfood(self.food.foodList)  # Vérifie si Pacman mange des food
        if food:  # Si Pacman a mangé un food
            self.food.numEaten += 1  # Incrémente le nombre de food mangés
            self.updateScore(food.points)  # Met à jour le score avec les points du food mangé
            if self.food.numEaten == 30:  # Si Pacman a mangé 30 food
                self.ghosts.inky.startNode.allowAccess(RIGHT, self.ghosts.inky)  # Autorise l'accès d'Inky à un nœud
            if self.food.numEaten == 70:  # Si Pacman a mangé 70 food
                self.ghosts.clyde.startNode.allowAccess(LEFT, self.ghosts.clyde)  # Autorise l'accès de Clyde à un nœud
            self.food.foodList.remove(food)  # Retire le food mangé de la liste
            if food.name == POWERFOOD:  # Si Pacman a mangé un power food
                self.ghosts.startFreight()  # Lance le mode 'freight' des fantômes
            if self.food.isEmpty():  # Si tous les food ont été mangés
                self.hideEntities()  # Cache les entités du jeu

    def checkGhostEvents(self):
        for ghost in self.ghosts:
            if self.pacman.collideGhost(ghost):  # Si Pacman entre en collision avec un fantôme
                if ghost.mode.current is FREIGHT:  # Si le fantôme est en mode 'freight'
                    self.pacman.visible = False  # Rend Pacman invisible
                    ghost.visible = False  # Rend le fantôme invisible
                    self.updateScore(ghost.points)  # Met à jour le score avec les points du fantôme
                    self.textgroup.addText(str(ghost.points), WHITE, ghost.position.x, ghost.position.y, 8,
                                           time=1)  # Affiche les points gagnés
                    self.ghosts.updatePoints()  # Met à jour les points des fantômes
                    ghost.startSpawn()  # Lance le processus de réapparition du fantôme
                    self.nodes.allowHomeAccess(ghost)  # Autorise l'accès du fantôme à la maison
                elif ghost.mode.current is not SPAWN:  # Si le fantôme n'est pas en mode 'spawn'
                    if not self.pacman.alive:  # Si Pacman est vivant
                        self.lives -= 1  # Décrémente le nombre de vies
                        self.lifesprites.removeImage()  # Supprime une vie à l'écran
                    if self.lives <= 0:  # Si toutes les vies ont été perdues
                        self.pacman.die()  # Fait mourir Pacman
                        self.ghosts.hide()  # Cache les fantômes
                        self.textgroup.showText(GAMEOVERTXT)

    def showEntities(self):
        self.pacman.visible = True  # Rend Pacman visible
        self.ghosts.show()  # Affiche les fantômes

    def hideEntities(self):
        self.pacman.visible = False  # Rend Pacman invisible
        self.ghosts.hide()  # Cache les fantômes

    def nextLevel(self):
        self.showEntities()  # Affiche les entités du jeu
        self.level += 1  # Incrémente le niveau
        self.startGame()  # Démarre le prochain niveau
        self.textgroup.updateLevel(self.level)  # Met à jour le texte du niveau

    def restartGame(self):
        self.lives = 5  # Réinitialise le nombre de vies
        self.level = 0  # Réinitialise le niveau
        self.startGame()  # Redémarre le jeu
        self.score = 0  # Réinitialise le score
        self.textgroup.updateScore(self.score)  # Met à jour le texte du score
        self.textgroup.updateLevel(self.level)  # Met à jour le texte du niveau
        self.textgroup.showText(READYTXT)  # Affiche le texte de prêt
        self.lifesprites.resetLives(self.lives)  # Réinitialise les vies

    def resetLevel(self):
        self.pacman.reset()  # Réinitialise Pacman
        self.ghosts.reset()  # Réinitialise les fantômes
        self.textgroup.showText(READYTXT)  # Affiche le texte de prêt

    def updateScore(self, points):
        self.score += points  # Ajoute les points au score total
        self.textgroup.updateScore(self.score)  # Met à jour le texte du score

    def render(self):
        self.screen.blit(self.background, (0, 0))  # Affiche l'arrière-plan à l'écran
        self.food.render(self.screen)  # Affiche les food à l'écran
        self.pacman.render(self.screen)  # Affiche Pacman à l'écran
        self.ghosts.render(self.screen)  # Affiche les fantômes à l'écran
        self.textgroup.render(self.screen)  # Affiche le texte à l'écran

        # Affiche les vies restantes à l'écran
        for i in range(len(self.lifesprites.images)):
            x = self.lifesprites.images[i].get_width() * i
            y = SCREENHEIGHT - self.lifesprites.images[i].get_height()
            self.screen.blit(self.lifesprites.images[i], (x, y))

        pygame.display.update()  # Met à jour l'affichage de l'écran


if __name__ == "__main__":
    game = Window()
    game.startGame()
    while True:
        game.update()
