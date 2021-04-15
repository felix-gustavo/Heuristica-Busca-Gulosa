from geopy import distance

class Node(object):
    def __init__(self, nome, x, y, obj):
        self.nome = nome
        self.adjacentes  = []

        self.x = x
        self.y = y

        self.distObj = 0 if obj is None else distance.distance((self.x, self.y), (obj.x, obj.y)).km

    def __lt__(self, other):
        return self.distObj < other.distObj