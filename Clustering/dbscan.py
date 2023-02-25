import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import math

class Node():
    def __init__(self, state, location) -> None:
        self.state = state
        self.loc = location
        self.visited = False
        self.cluster = None
        self.type = None
        self.neighbours = []

    def joinCluster(self, cluster):
        if self.cluster is not None:
            self.cluster.rmNode()
        cluster.addNode(self)


class Cluster():
    def __init__(self, state, node) -> None:
        self.state = state
        self.nodes = []
        self.addNode(node)

    def addNode(self, node):
        self.nodes.append(node)
        node.cluster = self

    def rmNode(self, node):
        self.nodes.remove(node)
        node.cluster = None


class DBSCAN():
    def __init__(self, nodes, epsilon = 1, minPoints = 6) -> None:
        self.nodes = nodes
        self.epsilon = epsilon
        self.minPoints = minPoints
        self.nodeTypes = ['core', 'border', 'isolated']

    def fit(self):
        for node in self.nodes:
            if node.visited:
                continue
            else:
                for onode in self.nodes:
                    if math.dist(node.loc, onode.loc) < self.epsilon:
                        node.neighbours.append(onode)
                    
                    if len(node.neighbours) == self.minPoints:
                        



def main():
    pass

if __name__ == '__main__':
    main()
