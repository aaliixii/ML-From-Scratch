import numpy as np
import matplotlib.pyplot as plt
import math

class Node():
    def __init__(self, state, location) -> None:
        self.state = state
        self.location = location
        self.visited = False

    def dist(self, node):
        return round(math.dist(self.location, node.location), 2)

class NHood():
    def __init__(self) -> None:
        self.neighbours = []

    def addNode(self, node):
        self.neighbours.append(node)

    def rmNode(self, node):
        self.neighbours.remove(node)

    def maxDist(self, node):
        dist = [math.dist(i.location, node.location) for i in self.neighbours]
        return (max(dist), self.neighbours[dist.index(max(dist))])

def plot(nodes, neighbours, target):
    x = []
    y = []
    c = []
    color = ['#FF5733', '#000000', '#2DAF00']

    for node in nodes:
        x.append(node.location[0])
        y.append(node.location[1])
        if node in neighbours:
            c.append(color[0])
        else:
            c.append(color[1])
        
    x.append(target.location[0])
    y.append(target.location[1])
    c.append(color[2])

    plt.scatter(x, y, c = c)
    plt.show()

def main():
    n = int(input('Number of Points'))

    x = [chr(ord('a') + i) for i in range(n)]
    d = [(np.random.randint(-10, 10), np.random.randint(-10, 10)) for i in range(n)]

    k = round(np.sqrt(n))

    nodes = []
    for i in range(len(x)):
        nodes.append(Node(x[i], d[i]))

    print(d)
    hood = NHood()
    target = Node('target', (0,0))

    for i, node in enumerate(nodes):
        if i<k:
            hood.addNode(node)
        else:
            if hood.maxDist(node)[0] > node.dist(target):
                hood.rmNode(hood.maxDist(node)[1])
                hood.addNode(node)

    for i in nodes:
        print(i.state, i.dist(target))

    for i in hood.neighbours:
        print(i.state)

    plot(nodes, hood.neighbours, target)
if __name__ == '__main__':
    main()