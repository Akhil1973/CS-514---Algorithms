def best(W, item):
    opt = [[0 for i in range(0, W + 1)] for j in range(0, len(item) + 1)]
    back = [[0 for i in range(0, W + 1)] for j in range(0, len(item) + 1)]

    for i, (w, v, c) in enumerate(item):
        i += 1
        for x in range(1, W + 1):
            for j in range(min(c, x // w) + 1):
                if x >= j * w and opt[i][x] < opt[i - 1][x - j * w] + j * v:
                    opt[i][x] = opt[i - 1][x - j * w] + j * v
                    back[i - 1][x] = j
    return opt[len(item)][W], _best(W, len(item) - 1,item, back)

def _best(w, i, item, back):
        if i < 0:
            return []
        new_w = w - item[i][0] * back[i][w]
        return _best(new_w, i - 1, item, back) + [back[i][w]]


if __name__ == "__main__":
    print(best(3, [(1, 5, 2), (1, 5, 3)]))

