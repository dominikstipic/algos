import numpy as np
from typing import List

class NamedMatrix():
    nodes: List[str] = []
    matrix: np.array = None

    def __init__(self, nodes: List[str]):
        self.nodes = nodes
        self.matrix = np.zeros([len(nodes), len(nodes)])

    def _index_of(self, letter: str) -> int:
        for i, a in enumerate(self.nodes):
            if a == letter:
                return i
        return -1
    
    def get_element_index(self, n: str) -> int:
        for i, ns in enumerate(self.nodes):
            if ns == n:
                return i
        return -1

    def __setitem__(self, indices, value):
        a, b = indices
        assert type(a) == str and type(b) == str
        i = self._index_of(a)
        j = self._index_of(b)
        self.matrix[i, j] = value

    def __getitem__(self, indices):
        i,j = indices
        if type(i) != slice:
            i = self._index_of(i)
        if type(j) != slice:
            j = self._index_of(j)
        elem = self.matrix[i,j]
        bs = elem == 1
        return  self.nodes[bs]