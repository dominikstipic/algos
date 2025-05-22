import numpy as np

def num_bg(xs: np.array, x: int) -> int:
    return (xs >= x).sum()

def calc_h_index(hs: list) -> int:
    hs = sorted(hs)
    HS = np.array(hs)
    h_prev = 0
    for i, h in enumerate(hs):
        cnt_bg = (HS >= h).sum()
        if cnt_bg == h:
            return h
        elif h > cnt_bg:
            return h_prev
        h_prev = h


cs0 = sorted([168, 47, 15, 11, 11, 11, 10, 9, 8, 8, 8, 8, 7, 6, 6, 5, 5, 5, 4, 4] + [3]*8 + [2]*8 + [1]*14)
cs1 = [10, 8, 5, 4, 3]
cs2 = [25, 8, 5, 3, 3]
cs5 = sorted([51, 22, 22, 15, 5, 5, 2, 1])
H = calc_h_index(cs0)
print(H)