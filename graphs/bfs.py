# Adjacency matrix -> columns and rows are the graphs and the value is True if the nodes are adjecent
# Adjacency list -> Each node keeps the list of its edge nodes
import pandas as pd
import graphs_factory as gf

G1 = gf.graph1()
G2 = gf.graph2()
G3 = gf.graph3()

nodes = ["K", "A", "X", "U"]
X = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]

# X, K, A, e(K)=A X (¤), e(A)=K¤ X¤ U, e(U) = A¤ 
# e(K) = A X
# e(A) = K X U

# expand the initial state -> EG
# go one by one in EG, expand the new states while ignoring already visited states. 

################################################################################
def expand(node, G):
    mask = G.loc[node] == 1
    return list(G.loc[node][mask].index)

def difference(xs: list, ys: list) -> list:
    for y in ys:
        if y in xs:
            idx = xs.index(y)
            xs.pop(idx)
    return xs

"""
Visit all next states. -> expanded list
After that expand the states in the LR order. 
THe new states should be included in the end result list

"""

"""
X = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [0, 1, 0, 0]
]

# X, K, A, e(K)=¤, e(A)=U, e(U) = ¤ 
# e(K) = A X
# e(A) = K X U

"""
def process():
    pass

def bfs(start_node, G):
    frontier = [start_node]
    explored = []
    while True:
        node = frontier[-1]
        explored.append(node)
        next_nodes = expand(node)
        for node in next_nodes:
            process(node)
            


start_node = "X"
trace1 = bfs(start_node, G1)
trace2 = bfs(start_node, G2)
trace3 = bfs(start_node, G3)

# Everything is correct