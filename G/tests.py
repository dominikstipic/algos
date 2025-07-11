from graph import Graph, Node, factory
import numpy as np

def test_alphabet_sort():
    nodes = ["G", "B", "A", "C", "D", "E", "F"]
    nodes = sorted(nodes)
    assert nodes == ["A", "B", "C", "D", "E", "F", "G"], "Lists does not match"

def test_expand():
    G = factory()
    expected = {Node("B"), Node("C"), Node("D")}
    elems = G.expand("A")
    assert elems == expected

def test_nm():
    nm = factory().named_matrix
    xs = nm["A", :]
    assert (xs == np.array(["B", "C", "D"])).all(), "FAILED"

