from node import Node as node


# Building the map
row = 6
col = 5
map = [[node() for x in range(col)] for y in range(row)]


for x in range(row):
    for y in range(col):
        map[x][y].pos = str(x) + str(y)


def main():
    for x in range(row):
        for y in range(col):
            print map[x][y].pos


if __name__ == '__main__':
    main()
