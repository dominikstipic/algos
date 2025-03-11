import string
import numpy as np
from typing import Tuple, List

class Words():
    path = "/usr/share/dict/words"

    def __init__(self):
        self.words = self.get_words()
        self.words = [w.upper() for w in self.words]

    def select(self, idx: int, letter: str):
        selected_words = [w for w in self.words if idx < len(w) and w[idx] == letter]
        return selected_words
    
    def select(self, prefix: str):
        selected_words = [w for w in self.words if w.startswith(prefix)]
        return selected_words

    def __getitem__(self, index):
        return self.words[index]

    def get_words(self):
        with open(self.path, "r") as fp:
            lines = fp.readlines()
            lines = [l.strip() for l in lines]
        return lines

class Boggle:
    words = Words()

    def __init__(self, N):
        uppercase_letters = list(string.ascii_uppercase)
        X = np.random.randint(0, len(uppercase_letters), size=(4, 4))
        self.X = np.vectorize(lambda i : uppercase_letters[i])(X)

    @staticmethod
    def create(X):
        B = Boggle(len(X))
        B.X = np.array(X)
        return B

    def __repr__(self):
        string = ""
        N = len(self.X)
        for i in range(N):
            row = ""
            for j in range(N):
                x = self.X[i,j]
                row += f"{x} " 
            string += row + "\n"
        return string
    
    def print(self, indices, tag="*"):
        string = ""
        N = len(self.X)
        for i in range(N):
            row = ""
            for j in range(N):
                x = self.X[i,j]
                if (i,j) in indices:
                    row += f"{x}{tag} " 
                else:
                    row += f"{x} " 
            string += row + "\n"
        return string


    def __getitem__(self, indices):
        i,j = indices
        return self.X[j,i]
    
    def _neighbour_index(self, x: int, y: int, k: int, x_lenght: int, y_length: int):
        xs = [
            (x-k, y),
            (x+k, y),
            (x, y+k),
            (x, y-k), 
            (x+1, y+1),
            (x-1, y-1),
            (x-1, y+1),
            (x+1, y-1),
        ]
        xs = [(x,y) for x,y in xs if (x >= 0 and y>=0)]
        xs = [(x,y) for x,y in xs if (x < x_lenght and y < y_length)]
        return xs

    def neigborhood(self, i, j) -> Tuple[list, list]:
        indices = self._neighbour_index(i, j, 1, len(self.X), len(self.X))
        xs = [self.X[x,y] for x,y in indices]
        return xs, indices
    
    def dictionary(self):
        words = self.words.get_words()
        words = [w.upper() for w in words]
        return words

def evaluate_trail(trail: List[Tuple[int, int]], boggle: Boggle):
    result = ""
    for x,y in trail:
        s = boggle[x,y]
        result += s
    return result

def extract_words(trails_next, boggle):
    to_delete = []
    result = []
    sentences = [evaluate_trail(ts, boggle) for ts in trails_next]
    for i, sentence in enumerate(sentences.copy()):
        if sentence in boggle.dictionary():
            result.append(sentence)
        selected = boggle.words.select(sentence)
        if len(selected) == 0:
            to_delete.append(i)
    trails_next = [ts for i,ts in enumerate(trails_next) if i not in to_delete]
    return result

def snake_search(letter: str, grid: np.array, boggle: Boggle):
    """
        Extend the frontier to the neighbours. 
        Retrieve the new letters. 
        prefixize. 
        Evalaute if this is a new word. 
        Store if this is a new word. 
    """
    trails = [[(0, 0), (1,1)]]
    trails_next = [] 
    human_words = []
    indices = []
    while True:
        for i,ts in enumerate(trails):
            x,y = ts[-1]
            _, neigbour_indices = boggle.neigborhood(x, y)
            neigbour_indices = [(x,y) for x,y in neigbour_indices if (x,y) not in trails[i]]
            if len(neigbour_indices) == 0:
                continue
            trails_next = [trails[i] + [(x,y)] for (x,y) in neigbour_indices]
            import pdb; pdb.set_trace()
            sentences = extract_words(trails_next, boggle)
            
            print(sentences)
            import pdb; pdb.set_trace()

        if trails_next == trails:
            break
        trails = trails_next 
    return indices, human_words


N = 4
#boggle = Boggle(4)

X = [
    ["H", "Q", "D", "D"],
    ["S", "E", "S", "S"],
    ["S", "L", "S", "S"],
    ["S", "L", "O", "S"]
]

b = Boggle.create(X)
print(b)

c = b.X[0, 0]
idx, words = snake_search(c, b.X, b)
print(words)

