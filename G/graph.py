import numpy as np
from matrix import NamedMatrix
from typing import List, Set

def factory():
    G = Graph(["B", "A", "C", "D", "E", "F", "G"])
    G.connect(Node("A"), Node("B"))
    G.connect(Node("A"), Node("C"))
    G.connect(Node("A"), Node("D"))

    G.connect(Node("B"), Node("A"))
    G.connect(Node("B"), Node("E"))
    G.connect(Node("B"), Node("F"))

    G.connect(Node("C"), Node("G"))

    G.connect(Node("D"), Node("A"))
    G.connect(Node("D"), Node("G"))

    G.connect(Node("G"), Node("D"))
    return G


class Node:
    value: str = None

    def __init__(self, node):
        self.value = node

    def __eq__(self, node):
        return self.value == node.value

    def __repr__(self):
        return self.value
    
    def __hash__(self):
        return hash(self.value)
    

class Graph:
    nodes : List[str] = []
    named_matrix: NamedMatrix = []

    def __init__(self, nodes: List[str]):
        self.nodes = np.array(sorted(nodes))
        self.named_matrix = NamedMatrix(self.nodes)

    def connect(self, node_start: Node, node_end: Node):
        self.named_matrix[node_start.value, node_end.value] = 1

    def connect_weight(self, node_start: Node, node_end: Node, weight: float):
        self.named_matrix[node_start.value, node_end.value] = weight

    def expand(self, node: Node) -> Set[Node]:
        if type(node) == str:
            node = Node(node)
        nodes = self.named_matrix[node.value, :]
        nodes = [Node(n) for n in nodes]
        return nodes

    def bfs(self, start_node: Node):
        open = [start_node]
        visited = [start_node]
        while len(open) != 0:
            n = open.pop()
            nodes = self.expand(n)
            for n in nodes:
                if n not in visited:
                    open.append(n)
                    visited.append(n)
        return visited
    
    def dfs(self, start_node: Node):
        open = [start_node]
        visited = [start_node]
        while len(open) != 0:
            n = open[0]
            visited.append(n)
            open = open[1:]
            nodes = self.expand(n)
            for n in nodes:
                if n not in visited:
                    open.append(n)
                    
        return visited
    
    def search(self, start_node: Node, end_goal: Node):
        """
            Works for direct graphs and not for the acyclical
        """
        open = [start_node]
        visited = set([start_node])
        while len(open) != 0:
            n = open.pop()
            if(n == end_goal):
                return visited
            nodes = self.expand(n)
            for n in nodes:
                if n not in visited:
                    open.append(n)
        return False
    

    def __getitem__(self, indices):
        i,j = indices
        return self.named_matrix[i, j]
    

g = factory()
xs= g.dfs(Node("A"))
print(xs)



