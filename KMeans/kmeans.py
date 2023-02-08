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

    def change(self, node, cluster):
        cluster.rmNode(node)
        self.addNode(node)


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

    means = []
    for z in range(0, epochs):
        print(f'{z+1} Iteration\n')
        mean = [i.mean() for i in clusters.values()]
        means.append(mean)
        # print('Mean: ', mean) #Debug
        selected = []
        for i, cluster in enumerate(clusters.values()):
            dist = []
            # print(f'{cluster.state}') #Debug
            print(mean[i]) #Debug

            for node in nodes:
                # print(node.state, node.cluster) #Debug

                if (float(node.loc[0]) != mean[i][0]) or (float(node.loc[1]) != mean[i][1]):
                    dist.append([node, math.dist(mean[i], node.loc)])
                    # dist1.append(math.dist(mean[i], node.loc)) #Debug
                    # print('Distance: ', dist1) #Debug
                else:
                    dist.append([node, 100])
            dist.sort(key = lambda i: i[1])

            for i in dist:
                if i[0] not in selected:
                    minNode = i[0]
                    selected.append(minNode)
                    break

            # print(minNode.state)    #Debug

            if minNode.cluster is None:
                cluster.addNode(minNode)
            else:
                cluster.change(minNode, clusters[minNode.cluster])
            # print('') #Debug

            # print('') #Debug
        plot(nodes, clusters, means)
        means = []
        for i in nodes:
            print(i.state, i.cluster)
    # plot(nodes, clusters, means)

if __name__ == '__main__':
    main()
