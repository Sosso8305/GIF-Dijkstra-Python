from node import Node

class Graph:
    def __init__(self,name,tikzpicture):
        self.name = name
        self.tikzpicture
        self.allNodes = set() #mathematical set for don't have twice times one node
        self.allLinks = []

    def addLink(self,link):
        self.allNodes.add(link.node1)
        self.allNodes.add(link.node2)
        self.allLinks.append(link)

    def addOnlyLink(self,link):
        self.allLinks.append(link)

    def addNode(self,node):
        self.allNodes.add(node)

    def copyTo(self):
        from copy import deepcopy
        return deepcopy(self)