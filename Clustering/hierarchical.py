import numpy as np
import math

class Clustering():
    def __init__(self, matrix, clusters, method = 'single') -> None:

        self.adj = matrix
        self.clusters = clusters
        self.threshold = 0
        self.k = len(self.clusters)

        if method == 'avg':
            self.averageLink()
        else:
            self.singleLink()

    def findThreshold(self):
        idx = []
        for i in range(len(self.adj)):
            for j in range(len(self.adj[0])):
                if self.adj[i][j] == self.threshold:
                    if (j, i) in idx:
                        continue
                    else:
                        idx.append((i, j))
        return idx

    def trashEmpty(self):
        c = []
        for cluster in self.clusters:
            if len(self.clusters[cluster].nodes) == 0:
                c.append(cluster)
        for i in c:
            del self.clusters[i]

    def newAdj(self):
        for i, cluster in enumerate(self.clusters.values()):
            if len(cluster.nodes) != 1:

                minNodes = cluster.minNode(self.clusters)
                dist = []

                for node in minNodes:
                    dist.append(math.dist(node.loc, minNodes[node].loc))
            
                minNode_from, minNode_to = list(minNodes.keys())[dist.index(min(dist))].state, list(minNodes.values())[dist.index(min(dist))].state

            for j, cluster in enumerate(self.clusters.values()):
                

            print(minNode_from, minNode_to)







    def singleLink(self):
        map = {i: j for i, j in enumerate(self.clusters.values())}
        self.threshold += 1
        idx = self.findThreshold()

        for e in idx:
            map[e[0]].addNodes(map[e[1]].nodes, map[e[1]])

        self.trashEmpty()

        # Debug
        for cluster in self.clusters.values():
            print(cluster.state, [i.state for i in cluster.nodes])
        
        self.newAdj()



    def averageLink(self):
        pass

class Cluster():
    def __init__(self, state, node) -> None:
        self.state = state
        self.nodes = []
        self.addNode(node)

    def addNode(self, node):
        self.nodes.append(node)
        self.cluster = self.state

    def addNodes(self, nodes, node_cluster):
        for node in nodes:
            node_cluster.rmNode(node)
            self.addNode(node)
    
    def rmNode(self, node):
        self.nodes.remove(node)
        node.cluster = None

    def minNode(self, clusters):
        minDist = {}

        for s_node in self.nodes:
            for cluster in clusters:
                dist = []
                if cluster != self.state:
                    for c_node in clusters[cluster].nodes:
                        dist.append(math.dist(s_node.loc, c_node.loc))
                    
                    minDist[s_node] = clusters[cluster].nodes[dist.index(min(dist))]
        
        return minDist

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
    distance = list(np.around(distance, 0))

    clusters = dict()
    for i, node in enumerate(nodes):
        clusters[f'k{i}'] = Cluster(f'k{i}', node)

    method = input('Clustering Algorithm')
    Clustering(matrix = distance, clusters = clusters, method = method)

if __name__ == '__main__':
    main()