import numpy as np
import matplotlib.pyplot as plt
import math
import random
import copy

class Node():
    def __init__(self, state, location) -> None:
        self.state = state
        self.loc = location
        self.cluster = None
        self.visited = False

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
        node.visited = True

    def rmNode(self, node):
        self.nodes.remove(node)
        node.cluster = None


def plot(nodes, clusters, means):
    x = []
    y = []
    mean_x = []
    mean_y = []
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
    for mean in means:
        mean_x.append(mean[0])
        mean_y.append(mean[1])
    plt.plot(mean_x, mean_y, '+r')
    plt.scatter(x, y, c=c)
    plt.show()

def visit_reset(nodes):
    for i in nodes:
        i.visited = False

def main():
    n = int(input('Number of Points:\n'))
    k = int(input('Number of Clusters:\n'))
    epochs = int(input('Number of Epochs\n'))
    x = [chr(ord('A') + i) for i in range(n)]
    d = [(np.random.randint(-5, 0), np.random.randint(-5, 0)) for i in range(n//2)] + [(np.random.randint(0, 5), np.random.randint(-5, 0)) for i in range(n//2)]
    # x = ['a', 'b', 'c', 'd', 'e']
    # d = [(0,0), (0,1), (1,0), (1,1), (2,0)]
    nodes = []
    for i in range(len(x)):
        nodes.append(Node(x[i], d[i]))

    clusters = dict()
    initial_points = random.sample(range(0, n), k)
    starter_nodes = []

    for i in range(0, k):
        starter_nodes.append(nodes[initial_points[i]])
        clusters[f'k{i+1}'] = Cluster(f'k{i+1}', nodes[initial_points[i]])

    print('')
    for i in nodes:
            print(i.state, i.cluster)
    print('')

if __name__ == '__main__':
    main()
