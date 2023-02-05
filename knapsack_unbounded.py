def best(W, items):

    unbounded = {0: (0, [0]*len(items))}
    def best_helper(W):
        if W not in unbounded:
            max = 0
            index = -1
            value = [0]*len(items)
            for i, item in enumerate(items):
                if W - item[0] >= 0:
                    v, a = best_helper(W - item[0])
                    if v + item[1] > max:
                        max = v + item[1]
                        index = i
                        value = list(a)
            if index != -1:
                value[index] += 1
            unbounded[W] = (max, value)
        return unbounded[W]
    return best_helper(W)


if __name__ == "__main__":
    print(best(3, [(1, 5), (1, 5)]))
