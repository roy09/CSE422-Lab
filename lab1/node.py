class Node:
    pos = ""
    neighbor = []
    visited = False

    def __unicode__(self):
        return self.pos
