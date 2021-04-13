from geopy import distance

class Node(object):
    def __init__(self, nome, x, y, dest):
        self.nome = nome
        self.adjacentes  = []
        self.visitado  = False
        self.x = x
        self.y = y

        self.distanciaObjetivo = self.calculaDistancia(dest)

    def calculaDistancia(self, dest):
        if dest is None: return 0

        return distance.distance((self.x, self.y), (dest.x, dest.y)).km