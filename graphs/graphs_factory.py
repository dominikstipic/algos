import pandas as pd
def graph1():
    # X K A U
    nodes = ["K", "A", "X", "U"]
    X = [
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 0],
        [0, 1, 0, 0]
    ]
    G = pd.DataFrame(data=X, columns=nodes, index=nodes)
    return G

def graph2():
    # X 9 7 ć
    adj_matrix_undirected = [
        [0, 1, 1, 0],  # Node 0: Connected to 1 and 2
        [1, 0, 0, 1],  # Node 1: Connected to 0 and 3
        [1, 0, 0, 0],  # Node 2: Connected to 0
        [0, 1, 0, 0]   # Node 3: Connected to 1
    ]
    nodes = ["9", "7", "X", "ć"]
    G = pd.DataFrame(data=adj_matrix_undirected, columns=nodes, index=nodes)
    return G

def graph3():
    # X Č V 1 
    adj_matrix_directed = [
        [0, 1, 0, 0],  # Node 0: Points to 1
        [0, 0, 1, 0],  # Node 1: Points to 2
        [0, 0, 0, 1],  # Node 2: Points to 3
        [1, 0, 0, 0]   # Node 3: Points to 0
    ]
    nodes = ["1", "X", "Č", "V"]
    G = pd.DataFrame(data=adj_matrix_directed, columns=nodes, index=nodes)
    return G

