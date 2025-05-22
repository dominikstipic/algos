from typing import List, Tuple

class Node:
    data  = None
    left  = None
    right = None 

    def __init__(self, data, left, right):
        self.data  = data
        self.left  = left
        self.right = right
    
    def __repr__(self):
        return f"Node[{self.data}, left={self.left.data}, right={self.right.data}]"
    
    # Less memory
    @staticmethod
    def _connect_by_level(xss: List[Tuple[list, int]], yss: List[Tuple[list, int]]):
        levels = [level for _, level in xss+yss]
        d = {l: [] for l in levels}
        for l in levels:
            pass  
        
    def print(self):
        print(f"{int(self.data)}", end=" ")
        if self.left == None and self.right == None:
            return
        self.left.print()
        self.right.print()
        
        
    def slice(self, level=0) -> List[Tuple[list, int]]:
        if self.left != None:
            # [([n1,n2,n3], L1)]
            left_nodes   = self.left.slice(level=level+1)
        if self.right != None:
            right_nodes  = self.right.slice(level=level+1)
        if self.right == None and self.left == None:
            return []
        levels = [l for _, l in (left_nodes + right_nodes)] + [level]
        result = {l: [] for l in levels}
        result[level].append(self.data)
        for node, level in (left_nodes + right_nodes):
            result[level].append(node)
        xs = []
        for l, x in result.items():
            xs.append((l, x))
        return xs

def factory(n):
    def factory_inner(n, i):
        count = lambda n : 2**(n)-1
        total_n = count(n)
        total_n_1 = count(n-1)
        leafs = total_n - total_n_1
        leaf_labels = list(range((total_n-leafs)+1,total_n+1))
        nodes = [[Node(label, None, None) for label in leaf_labels]]
        for j in range(n):
            ns = []
            for i in range(len(nodes[-1])):
                if len(nodes[-1]) == 1:
                    break
                if i % 2 == 0:
                    n = nodes[-1][i]
                    n = Node(n.data/2, nodes[-1][i], nodes[-1][i+1])
                    ns.append(n)
            nodes.append(ns)
        return nodes[-2]
    return factory_inner(n, 1)[0]

n = factory(4)
n.print()