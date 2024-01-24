from nodes import Node


class Map(object):
    def __init__(self):
        # Indentation des node de la map

        self.nodeA = Node(10, 10)
        self.nodeB = Node(1190, 10)
        self.nodeC = Node(1190, 690)
        self.nodeD = Node(10, 690)

        self.nodeE1 = Node(30, 30)
        self.nodeF1 = Node(280, 30)
        self.nodeG1 = Node(280, 130)
        self.nodeH1 = Node(290, 130)
        self.nodeI1 = Node(290, 30)
        self.nodeJ1 = Node(910, 30)
        self.nodeK1 = Node(910, 130)
        self.nodeL1 = Node(920, 130)
        self.nodeM1 = Node(920, 30)
        self.nodeN1 = Node(1170, 30)

        self.nodeE2 = Node(30, 670)
        self.nodeF2 = Node(280, 670)
        self.nodeG2 = Node(280, 570)
        self.nodeH2 = Node(290, 570)
        self.nodeI2 = Node(290, 670)
        self.nodeJ2 = Node(910, 670)
        self.nodeK2 = Node(910, 570)
        self.nodeL2 = Node(920, 570)
        self.nodeM2 = Node(920, 670)
        self.nodeN2 = Node(1170, 670)

        self.nodeO1 = Node(380, 120)
        self.nodeP1 = Node(810, 120)
        self.nodeQ1 = Node(810, 130)
        self.nodeR1 = Node(380, 130)

        self.nodeO2 = Node(380, 570)
        self.nodeP2 = Node(810, 570)
        self.nodeQ2 = Node(810, 580)
        self.nodeR2 = Node(380, 580)

        self.nodeS1 = Node(190, 120)
        self.nodeT1 = Node(140, 120)
        self.nodeU1 = Node(140, 290)
        self.nodeV1 = Node(150, 290)
        self.nodeW1 = Node(150, 130)
        self.nodeX1 = Node(190, 130)

        self.nodeS2 = Node(190, 580)
        self.nodeT2 = Node(140, 580)
        self.nodeU2 = Node(140, 410)
        self.nodeV2 = Node(150, 410)
        self.nodeW2 = Node(150, 570)
        self.nodeX2 = Node(190, 570)

        self.nodeS3 = Node(1010, 120)
        self.nodeT3 = Node(1060, 120)
        self.nodeU3 = Node(1060, 290)
        self.nodeV3 = Node(1050, 290)
        self.nodeW3 = Node(1050, 130)
        self.nodeX3 = Node(1010, 130)

        self.nodeS4 = Node(1010, 580)
        self.nodeT4 = Node(1060, 580)
        self.nodeU4 = Node(1060, 410)
        self.nodeV4 = Node(1050, 410)
        self.nodeW4 = Node(1050, 570)
        self.nodeX4 = Node(1010, 570)

        self.nodeY1 = Node(240, 280)
        self.nodeZ1 = Node(290, 280)
        self.nodeAA1 = Node(290, 295)
        self.nodeAB1 = Node(240, 295)

        self.nodeY2 = Node(240, 405)
        self.nodeZ2 = Node(290, 405)
        self.nodeAA2 = Node(290, 420)
        self.nodeAB2 = Node(240, 420)

        self.nodeY3 = Node(910, 405)
        self.nodeZ3 = Node(960, 405)
        self.nodeAA3 = Node(960, 420)
        self.nodeAB3 = Node(910, 420)

        self.nodeY4 = Node(910, 280)
        self.nodeZ4 = Node(960, 280)
        self.nodeAA4 = Node(960, 295)
        self.nodeAB4 = Node(910, 295)

        self.nodeAC = Node(750, 280)
        self.nodeAD = Node(810, 280)
        self.nodeAE = Node(810, 420)
        self.nodeAF = Node(380, 420)
        self.nodeAG = Node(380, 280)
        self.nodeAH = Node(440, 280)
        self.nodeAI = Node(440, 295)
        self.nodeAJ = Node(395, 295)
        self.nodeAK = Node(395, 405)
        self.nodeAL = Node(795, 405)
        self.nodeAM = Node(795, 295)
        self.nodeAN = Node(750, 295)

        self.connect_nodes()

        self.nodeList = [self.nodeA, self.nodeB, self.nodeC, self.nodeD,
                         self.nodeE1, self.nodeF1, self.nodeG1, self.nodeH1, self.nodeI1, self.nodeJ1, self.nodeK1, self.nodeL1,
                         self.nodeM1, self.nodeN1,
                         self.nodeE2, self.nodeF2, self.nodeG2, self.nodeH2, self.nodeI2, self.nodeJ2, self.nodeK2, self.nodeL2,
                         self.nodeM2, self.nodeN2,
                         self.nodeO1, self.nodeP1, self.nodeQ1, self.nodeR1,
                         self.nodeO2, self.nodeP2, self.nodeQ2, self.nodeR2,
                         self.nodeS1, self.nodeT1, self.nodeU1, self.nodeV1, self.nodeW1, self.nodeX1,
                         self.nodeS2, self.nodeT2, self.nodeU2, self.nodeV2, self.nodeW2, self.nodeX2,
                         self.nodeS3, self.nodeT3, self.nodeU3, self.nodeV3, self.nodeW3, self.nodeX3,
                         self.nodeS4, self.nodeT4, self.nodeU4, self.nodeV4, self.nodeW4, self.nodeX4,
                         self.nodeY1, self.nodeZ1, self.nodeAA1, self.nodeAB1,
                         self.nodeY2, self.nodeZ2, self.nodeAA2, self.nodeAB2,
                         self.nodeY3, self.nodeZ3, self.nodeAA3, self.nodeAB3,
                         self.nodeY4, self.nodeZ4, self.nodeAA4, self.nodeAB4,
                         self.nodeAC, self.nodeAD, self.nodeAE, self.nodeAF, self.nodeAG, self.nodeAH, self.nodeAI, self.nodeAJ, self.nodeAK, self.nodeAL, self.nodeAM, self.nodeAN
                         ]

    def connect_nodes(self):
        # Connections des nodes
        Node.connect_nodes(self.nodeA, 'RIGHT', self.nodeB)
        Node.connect_nodes(self.nodeB, 'DOWN', self.nodeC)
        Node.connect_nodes(self.nodeC, 'LEFT', self.nodeD)
        Node.connect_nodes(self.nodeD, 'UP', self.nodeA)

        Node.connect_nodes(self.nodeE1, 'RIGHT', self.nodeF1)
        Node.connect_nodes(self.nodeF1, 'DOWN', self.nodeG1)
        Node.connect_nodes(self.nodeG1, 'RIGHT', self.nodeH1)
        Node.connect_nodes(self.nodeH1, 'UP', self.nodeI1)
        Node.connect_nodes(self.nodeI1, 'RIGHT', self.nodeJ1)
        Node.connect_nodes(self.nodeJ1, 'DOWN', self.nodeK1)
        Node.connect_nodes(self.nodeK1, 'RIGHT', self.nodeL1)
        Node.connect_nodes(self.nodeL1, 'UP', self.nodeM1)
        Node.connect_nodes(self.nodeM1, 'RIGHT', self.nodeN1)

        Node.connect_nodes(self.nodeE1, 'DOWN', self.nodeE2)
        Node.connect_nodes(self.nodeN1, 'DOWN', self.nodeN2)

        Node.connect_nodes(self.nodeE2, 'RIGHT', self.nodeF2)
        Node.connect_nodes(self.nodeF2, 'UP', self.nodeG2)
        Node.connect_nodes(self.nodeG2, 'RIGHT', self.nodeH2)
        Node.connect_nodes(self.nodeH2, 'DOWN', self.nodeI2)
        Node.connect_nodes(self.nodeI2, 'RIGHT', self.nodeJ2)
        Node.connect_nodes(self.nodeJ2, 'UP', self.nodeK2)
        Node.connect_nodes(self.nodeK2, 'RIGHT', self.nodeL2)
        Node.connect_nodes(self.nodeL2, 'DOWN', self.nodeM2)
        Node.connect_nodes(self.nodeM2, 'RIGHT', self.nodeN2)

        Node.connect_nodes(self.nodeO1, 'RIGHT', self.nodeP1)
        Node.connect_nodes(self.nodeP1, 'DOWN', self.nodeQ1)
        Node.connect_nodes(self.nodeQ1, 'LEFT', self.nodeR1)
        Node.connect_nodes(self.nodeR1, 'UP', self.nodeO1)

        Node.connect_nodes(self.nodeO2, 'RIGHT', self.nodeP2)
        Node.connect_nodes(self.nodeP2, 'DOWN', self.nodeQ2)
        Node.connect_nodes(self.nodeQ2, 'LEFT', self.nodeR2)
        Node.connect_nodes(self.nodeR2, 'UP', self.nodeO2)

        Node.connect_nodes(self.nodeS1, 'LEFT', self.nodeT1)
        Node.connect_nodes(self.nodeT1, 'DOWN', self.nodeU1)
        Node.connect_nodes(self.nodeU1, 'RIGHT', self.nodeV1)
        Node.connect_nodes(self.nodeV1, 'UP', self.nodeW1)
        Node.connect_nodes(self.nodeW1, 'RIGHT', self.nodeX1)
        Node.connect_nodes(self.nodeX1, 'RIGHT', self.nodeS1)

        Node.connect_nodes(self.nodeS2, 'LEFT', self.nodeT2)
        Node.connect_nodes(self.nodeT2, 'UP', self.nodeU2)
        Node.connect_nodes(self.nodeU2, 'RIGHT', self.nodeV2)
        Node.connect_nodes(self.nodeV2, 'DOWN', self.nodeW2)
        Node.connect_nodes(self.nodeW2, 'RIGHT', self.nodeX2)
        Node.connect_nodes(self.nodeX2, 'DOWN', self.nodeS2)

        Node.connect_nodes(self.nodeS3, 'RIGHT', self.nodeT3)
        Node.connect_nodes(self.nodeT3, 'DOWN', self.nodeU3)
        Node.connect_nodes(self.nodeU3, 'LEFT', self.nodeV3)
        Node.connect_nodes(self.nodeV3, 'UP', self.nodeW3)
        Node.connect_nodes(self.nodeW3, 'LEFT', self.nodeX3)
        Node.connect_nodes(self.nodeX3, 'UP', self.nodeS3)

        Node.connect_nodes(self.nodeS4, 'RIGHT', self.nodeT4)
        Node.connect_nodes(self.nodeT4, 'UP', self.nodeU4)
        Node.connect_nodes(self.nodeU4, 'LEFT', self.nodeV4)
        Node.connect_nodes(self.nodeV4, 'DOWN', self.nodeW4)
        Node.connect_nodes(self.nodeW4, 'LEFT', self.nodeX4)
        Node.connect_nodes(self.nodeX4, 'DOWN', self.nodeS4)

        Node.connect_nodes(self.nodeY1, 'RIGHT', self.nodeZ1)
        Node.connect_nodes(self.nodeZ1, 'DOWN', self.nodeAA1)
        Node.connect_nodes(self.nodeAA1, 'LEFT', self.nodeAB1)
        Node.connect_nodes(self.nodeAB1, 'UP', self.nodeY1)

        Node.connect_nodes(self.nodeY2, 'RIGHT', self.nodeZ2)
        Node.connect_nodes(self.nodeZ2, 'DOWN', self.nodeAA2)
        Node.connect_nodes(self.nodeAA2, 'LEFT', self.nodeAB2)
        Node.connect_nodes(self.nodeAB2, 'UP', self.nodeY2)

        Node.connect_nodes(self.nodeY3, 'RIGHT', self.nodeZ3)
        Node.connect_nodes(self.nodeZ3, 'DOWN', self.nodeAA3)
        Node.connect_nodes(self.nodeAA3, 'LEFT', self.nodeAB3)
        Node.connect_nodes(self.nodeAB3, 'UP', self.nodeY3)

        Node.connect_nodes(self.nodeY4, 'RIGHT', self.nodeZ4)
        Node.connect_nodes(self.nodeZ4, 'DOWN', self.nodeAA4)
        Node.connect_nodes(self.nodeAA4, 'LEFT', self.nodeAB4)
        Node.connect_nodes(self.nodeAB4, 'UP', self.nodeY4)

        Node.connect_nodes(self.nodeAC, 'RIGHT', self.nodeAD)
        Node.connect_nodes(self.nodeAD, 'DOWN', self.nodeAE)
        Node.connect_nodes(self.nodeAE, 'LEFT', self.nodeAF)
        Node.connect_nodes(self.nodeAF, 'UP', self.nodeAG)
        Node.connect_nodes(self.nodeAG, 'RIGHT', self.nodeAH)
        Node.connect_nodes(self.nodeAH, 'DOWN', self.nodeAI)
        Node.connect_nodes(self.nodeAI, 'LEFT', self.nodeAJ)
        Node.connect_nodes(self.nodeAJ, 'DOWN', self.nodeAK)
        Node.connect_nodes(self.nodeAK, 'RIGHT', self.nodeAL)
        Node.connect_nodes(self.nodeAL, 'UP', self.nodeAM)
        Node.connect_nodes(self.nodeAM, 'LEFT', self.nodeAN)
        Node.connect_nodes(self.nodeAN, 'UP', self.nodeAC)

