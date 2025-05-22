class Tree:
    data: int = None
    left = None
    right = None

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def subtree(self, tree):
        if self.data != tree.data:
            self.left.subtree(tree)
        elif self.data != tree.data and self.left == None and self.right == None:
            return False
    
    def _depth(self):
        if self.left == None and self.right == None:
            return 1
        depth_left = self.left._depth()
        depth_right = self.right._depth()
        return max(depth_left, depth_right)+1
    
    def depth(self):
        return self._depth()-1
        
    def _levels(self, level=0):
        if self.left == None and self.right == None:
            return [(self.data, level)]
        xs_left  = self.left._levels(level+1)
        xs_right = self.right._levels(level+1)
        xs_middle = [(self.data, level)]
        return xs_left + xs_middle + xs_right
    
    def levels(self):
        ls = self._levels()
        d = self.depth()
        result = {i:[] for i in range(d+1)}
        for x, l in ls:
            result[l].append(x)
        return result

    def _lmr(self):
        if self.left == None and self.right == None:
            print(self.data, end=" ")
            return
        self.left._print("lmr")
        print(self.data, end=" ")
        self.right._print("lmr")

    def _mlr(self):
        if self.left == None and self.right == None:
            print(self.data, end=" ")    
            return
        print(self.data, end=" ")
        self.left._print("mlr")
        self.right._print("mlr")

    def _rml(self):
        if self.left == None and self.right == None:
            print(self.data, end=" ")    
            return
        self.right._print("rml")
        print(self.data, end=" ")
        self.left._print("rml")

    def _print(self, option="lmr"):
        assert(option in ["lmr", "mlr", "rml"])
        if option == "lmr":
            self._lmr()
        elif option == "mlr":
            self._mlr()
        else:
            self._rml()

    def print(self, option="lmr"):
        self._print(option)
        print()

def tree():
    l1 = Tree(6, None, None)
    l2 = Tree(10, None, None)
    l3 = Tree(11, None, None)
    l4 = Tree(1, None, None)
    k1 = Tree(5, l2, l3)
    j = Tree(7, l1, k1)
    v = Tree(4, j, l4)
    return v

t = tree()
ls = t.levels()
print(ls)