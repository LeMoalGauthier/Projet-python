from constants import *


class CarteBase(object):
    def __init__(self):
        self.hommenodeconnectLeft = None
        self.hommenodeconnectright = None
        self.portalPairs = {}
        self.homeoffset = (0, 0)
        self.ghostNodeDeny = {UP: (), DOWN: (), LEFT: (), RIGHT: ()}

    def connectHomeNodes(self, nodes):
        key = nodes.createHomeNodes(*self.homeoffset)
        nodes.connectHomeNodes(key, self.hommenodeconnectLeft, LEFT)
        nodes.connectHomeNodes(key, self.hommenodeconnectright, RIGHT)

    def setPortalPairs(self, nodes):
        for pair in list(self.portalPairs.values()):
            nodes.setPortalPair(*pair)

    def addOffset(self, x, y):
        return x + self.homeoffset[0], y + self.homeoffset[1]

    def denyGhostAccess(self, ghosts, nodes):
        nodes.denyGhostAccessList(*(self.addOffset(2, 3) + (LEFT, ghosts)))
        nodes.denyGhostAccessList(*(self.addOffset(2, 3) + (RIGHT, ghosts)))

        for direction in list(self.ghostNodeDeny.keys()):
            for values in self.ghostNodeDeny[direction]:
                nodes.denyGhostAccessList(*(values + (direction, ghosts)))