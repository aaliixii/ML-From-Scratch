import numpy as np
import matplotlib.pyplot as plt
import math

class Node():
    def __init__(self, state, location) -> None:
        self.state = state
        self.location = location

    def dist(self, node):
        return round(math.dist(self.location, node.location), 2)


def plot(nodes, neighbours, target):
    x = []
    y = []
    c = []
    color = ['#FF5733', '#000000', '#2DAF00']

    for node in nodes:
        x.append(node.location[0])
        y.append(node.location[1])
        if node.state in neighbours:
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
    k = int(input('No of Nearest Neighbours'))
    x = [chr(ord('a') + i) for i in range(n)]
    d = [(np.random.randint(-10, 10), np.random.randint(-10, 10)) for i in range(n)]

    nodes = []
    for i in range(len(x)):
        nodes.append(Node(x[i], d[i]))

    target = Node('target', (np.random.randint(-10, 10), np.random.randint(-10, 10)))
    dist = [[i.state, i.dist(target)] for i in nodes]
    dist.sort(key = lambda i: i[1])
    neighbours = [dist[i][0] for i in range(k)]

    plot(nodes, neighbours, target)

if __name__ == '__main__':
    main()

