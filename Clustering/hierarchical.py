import numpy as np
import math

class Clustering():
    def __init__(self, matrix, clusters, method = 'single', threshold = 2) -> None:

        self.adj = matrix
        self.clusters = clusters
        self.threshold = threshold

        self.k = len(self.clusters)

        if method == 'avg':
            self.averageLink(matrix)
        else:
            self.singleLink(matrix)

    def singleLink(self):
        while self.k != 1:
            for i in len(self.adj):
                for j in len(len(self.adj[0])):
                    if self.adj[i][j]

    def averageLink(self):
        pass

class Cluster():
    def __init__(self, state, node) -> None:
        self.state = state
        self.nodes = []

    def addNode(self, node):
        self.nodes.append(node)
        self.cluster = self.state

class Node():
    def __init__(self, state, loc) -> None:
        self.state = state
        self.loc = loc
        self.cluster = None


def main():
    n = int(input('Number of Points:\n'))
    x = [chr(ord('A') + i) for i in range(n)]
    d = [(np.random.randint(-5, 5), np.random.randint(-5, 5)) for i in range(n)]

    nodes = [Node(i[0], i[1]) for i in zip(x, d)]
    
    distance = []

    for target in nodes:
        dist = []
        for node in nodes:
            dist.append(math.dist(target.loc, node.loc))
        distance.append(dist)

    method = input('Clustering Algorithm')
    Clustering(matrix = distance, method = method)

if __name__ == '__main__':
    main()