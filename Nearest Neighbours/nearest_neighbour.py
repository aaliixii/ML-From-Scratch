import numpy as np
import matplotlib.pyplot as plt
import random
import math
class Node():
    def __init__(self, state, location) -> None:
        self.state = state
        self.location = location
        self.visited = False
        self.cluster = None

class Cluster():
    def __init__(self, state, node) -> None:
        self.state = state
        self.nodes = []
        self.addNode(node)

    def addNode(self, node):
        node.cluster = self.state
        self.nodes.append(node)
        node.visited = True

    def minDist(self, node):
        dist = (math.dist(i.location, node.location) for i in self.nodes)
        return min(dist)

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
        x.append(node.location[0])
        y.append(node.location[1])
        clust.append(node.cluster)
        for i in clusters:
            if node.cluster == i:
                c.append(clust_colours[i])
    
    plt.scatter(x, y, c=c)
    plt.show()

def mincluster(clusters, node):
    mindist = []
    for cluster in clusters.values():
        mindist.append([cluster.minDist(node)])
    return list(clusters.keys())[mindist.index(min(mindist))]

def main():

    n = int(input('Number of Points'))


    x = [chr(ord('A') + i) for i in range(n)]
    d = [(np.random.randint(-10, 10), np.random.randint(-10, 10)) for i in range(n)]

    print(x)
    print(d)

    critical_dist = 5
    k = 1

    nodes = []
    for i in range(len(x)):
        nodes.append(Node(x[i], d[i]))

    clusters = dict()
    clusters['k1'] = Cluster('k1', nodes[np.random.randint(0,5)])

    for node in (i for i in nodes if not i.visited):

        if clusters[mincluster(clusters, node)].minDist(node) <= critical_dist:
            clusters[mincluster(clusters, node)].addNode(node)
        else:
            k+=1
            clusters[f'k{k}'] = Cluster(f'k{k}', node)
    
    for node in nodes:
        print(node.state, node.cluster)
    plot(nodes, clusters)


if __name__ == '__main__':
    main()
