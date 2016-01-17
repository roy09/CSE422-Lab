class Node:
    pos = ""
    visited = False

    def __init__(self, neighbors=None):
        if neighbors is not None:
            self.neighbors = neighbors
        else:
            self.neighbors = []
        self.prev = None

    def __str__(self):
        return self.pos

    def add(self, sth):
        self.neighbors.append(sth)
