import numpy as np
import matplotlib.pyplot as plt
import math
import random

class Node():
    def __init__(self, state, location) -> None:
        self.state = state
        self.loc = location
        self.cluster = None

class Cluster():
    def __init__(self, state, node) -> None:
        self.state = state
        self.nodes = []
        self.addNode(node)
    
    def mean(self):
        mean_x = []
        mean_y = []
        for i in self.nodes:
            mean_x.append(i.loc[0])
            mean_y.append(i.loc[1])
        return np.mean([mean_x, mean_y], axis = 1)

    def addNode(self, node):
        node.cluster = self.state
        self.nodes.append(node)

    def rmNode(self, node):
        self.nodes.remove(node)

    def change(self, node, cluster):
        if len(self.nodes) > 1:
            self.rmNode(node)
            cluster.addNode(node)
        else:
            pass
def plot(nodes, clusters):
    x = []
    y = []
    clusters = list(clusters.keys())
    clust_colours = dict()
    c = []
    clust = []
    r = lambda: random.randint(0,255)
    for i in clusters:
        clust_colours[i] = '#%02X%02X%02X' % (r(),r(),r())

    for node in nodes:
        x.append(node.loc[0])
        y.append(node.loc[1])

        if node.cluster == None:
            c.append('#000000')
        else:
            for i in clusters:
                if node.cluster == i:
                    c.append(clust_colours[i])
    
    plt.scatter(x, y, c=c)
    plt.show()

def main():
    n = int(input('Number of Points:\n'))
    k = int(input('Number of Clusters:\n'))
    epochs = int(input('Number of Epochs:\n'))
    x = [chr(ord('A') + i) for i in range(n)]
    d = [(np.random.randint(-10, 10), np.random.randint(-10, 10)) for i in range(n)]

    nodes = []
    for i in range(len(x)):
        nodes.append(Node(x[i], d[i]))

    clusters = dict()
    intial_points = np.random.randint(0,len(x), size=k)

    for i in range(0, k):
        clusters[f'k{i+1}'] = Cluster(f'k{i+1}', nodes[intial_points[i]])

    for e in range(epochs):
        mean = [i.mean() for i in clusters.values()]
        for i, cluster in enumerate(clusters.values()):
            dist = []

            for node in nodes:
                dist.append(math.dist(mean[i], node.loc))

            minNode = nodes[dist.index(min(dist))]
            try:
                clusters[minNode.cluster].change(minNode, cluster)
            except KeyError:
                cluster.addNode(minNode)

    for node in nodes:
        print(node.state, node.cluster)
    for i in clusters.values():
        print(i.state, [j.state for j in i.nodes])

    plot(nodes, clusters)

if __name__ == '__main__':
    main()
