import pygame
import sys
from vector import Vector2
from constants import *
from nodes import Node

# Initialisation de Pygame
pygame.init()

# Définir les dimensions de la fenêtre
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

# Créer la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Node Test")

# Créer quelques nœuds

nodeA = Node(10, 10)
nodeB = Node(1190, 10)
nodeC = Node(1190, 690)
nodeD = Node(10, 690)

nodeE1 = Node(30, 30)
nodeF1 = Node(280, 30)
nodeG1 = Node(280, 130)
nodeH1 = Node(290, 130)
nodeI1 = Node(290, 30)
nodeJ1 = Node(910, 30)
nodeK1 = Node(910, 130)
nodeL1 = Node(920, 130)
nodeM1 = Node(920, 30)
nodeN1 = Node(1170, 30)

nodeE2 = Node(30, 670)
nodeF2 = Node(280,670)
nodeG2 = Node(280, 570)
nodeH2 = Node(290, 570)
nodeI2 = Node(290, 670)
nodeJ2 = Node(910, 670)
nodeK2 = Node(910, 570)
nodeL2 = Node(920, 570)
nodeM2 = Node(920, 670)
nodeN2 = Node(1170, 670)

# Connections des nodes
Node.connect_nodes(nodeA, 'RIGHT', nodeB, 'DOWN')
Node.connect_nodes(nodeB, 'DOWN', nodeC, 'LEFT')
Node.connect_nodes(nodeC, 'LEFT', nodeD, 'UP')

Node.connect_nodes(nodeE1, 'RIGHT', nodeF1, 'DOWN')
Node.connect_nodes(nodeF1, 'DOWN', nodeG1, 'RIGHT')
Node.connect_nodes(nodeG1, 'RIGHT', nodeH1, 'UP')
Node.connect_nodes(nodeH1, 'UP', nodeI1, 'RIGHT')
Node.connect_nodes(nodeI1, 'RIGHT', nodeJ1, 'DOWN')
Node.connect_nodes(nodeJ1, 'DOWN', nodeK1, 'RIGHT')
Node.connect_nodes(nodeK1, 'RIGHT', nodeL1, 'UP')
Node.connect_nodes(nodeL1, 'UP', nodeM1, 'RIGHT')
Node.connect_nodes(nodeM1, 'RIGHT', nodeN1, 'DOWN')

Node.connect_nodes(nodeE1, 'DOWN', nodeE2, 'RIGHT')
Node.connect_nodes(nodeN1, 'DOWN', nodeN2, 'RIGHT')

Node.connect_nodes(nodeE2, 'RIGHT', nodeF2, 'UP')
Node.connect_nodes(nodeF2, 'UP', nodeG2, 'RIGHT')
Node.connect_nodes(nodeG2, 'RIGHT', nodeH2, 'DOWN')
Node.connect_nodes(nodeH2, 'DOWN', nodeI2, 'RIGHT')
Node.connect_nodes(nodeI2, 'RIGHT', nodeJ2, 'UP')
Node.connect_nodes(nodeJ2, 'UP', nodeK2, 'RIGHT')
Node.connect_nodes(nodeK2, 'RIGHT', nodeL2, 'DOWN')
Node.connect_nodes(nodeL2, 'DOWN', nodeM2, 'RIGHT')
Node.connect_nodes(nodeM2, 'RIGHT', nodeN2, 'UP')


nodeList = [nodeA, nodeB, nodeC, nodeD,
            nodeE1, nodeF1, nodeG1, nodeH1, nodeI1, nodeJ1, nodeK1, nodeL1, nodeM1, nodeN1,
            nodeE2, nodeF2, nodeG2, nodeH2, nodeI2, nodeJ2, nodeK2, nodeL2, nodeM2, nodeN2]

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