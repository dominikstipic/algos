# Adjacency matrix -> columns and rows are the graphs and the value is True if the nodes are adjecent
# Adjacency list -> Each node keeps the list of its edge nodes
import pandas as pd
import graphs_factory as gf

G1 = gf.graph1()
G2 = gf.graph2()
G3 = gf.graph3()

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

def dfs(start_node, G, visited=[]):
    result = [start_node]
    while True:
        expanded = expand(start_node, G)
        expanded = difference(expanded, visited)
        if not expanded:
            break
        for e in expanded:
            if e not in result:
                visited = set(visited).union(set(result))
                rs = dfs(e, G, visited=list(visited))
                result += rs
        break
    return result


start_node = "X"
trace1 = dfs(start_node, G1)
trace2 = dfs(start_node, G2)
trace3 = dfs(start_node, G3)

# Everything is correct