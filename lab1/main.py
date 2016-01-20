from node import Node as node


# declaring the grid size and blocked pos\\
row = 6
col = 5
blockedPositions = ["02", "10", "21", "23", "43", "50"]
startPos = "31"
endPos = "04"

# Building the grid
grid = [[node() for x in range(col)] for y in range(row)]

for x in range(row):
    for y in range(col):
        grid[x][y].pos = str(x) + str(y)


# building neighbors
for x in range(row):
    for y in range(col):
        # TDRL
        try:
            if grid[x][y + 1].pos not in blockedPositions:
                grid[x][y].add(grid[x][y + 1])
        except IndexError:
            pass
        if y > 0:
            try:
                if grid[x][y - 1].pos not in blockedPositions:
                    grid[x][y].add(grid[x][y - 1])
            except IndexError:
                pass
        try:
            if grid[x + 1][y].pos not in blockedPositions:
                grid[x][y].add(grid[x + 1][y])
        except IndexError:
            pass
        if x > 0:
            try:
                if grid[x - 1][y].pos not in blockedPositions:
                    grid[x][y].add(grid[x - 1][y])
            except IndexError:
                pass


path = []
head = grid[3][1]
path.append(head)
lastNode = None


def listPrint(list):
    for k in list:
        print k,


def bfs():
    while(path):
        # print listPrint(path)
        currentNode = path.pop()
        print "Current Node: ", currentNode.pos

        currentNode.visited = True
        if currentNode.pos == endPos:
            lastNode = currentNode
            break
        else:
            for tempNode in currentNode.neighbors:
                if not tempNode.visited:
                    path.insert(0, tempNode)
                    tempNode.prev = currentNode

    print "Traversed path: ",
    while lastNode.prev:
        print lastNode
        lastNode = lastNode.prev
    print lastNode


def dfs():
    while(path):
        print listPrint(path)
        currentNode = path.pop()
        print "Current Node: ", currentNode.pos

        currentNode.visited = True
        if currentNode.pos == endPos:
            lastNode = currentNode
            break
        else:
            for tempNode in currentNode.neighbors:
                if not tempNode.visited and tempNode not in path:
                    path.append(tempNode)
                    tempNode.prev = currentNode

    print "Traversed path: ",
    while lastNode.prev:
        print lastNode,
        lastNode = lastNode.prev
    print lastNode


if __name__ == "__main__":
    # bfs()
    dfs()
