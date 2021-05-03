"""
https://www.algoexpert.io/questions/Depth-first%20Search
"""


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):

        currNode = self.name
        array.append(currNode)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
