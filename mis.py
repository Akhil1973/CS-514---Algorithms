
def max_wis(a):
    res = {-1:(0, []), 0:(0, [])}
    def f(len):
        if len not in res:
            (x, x_s) = f(len-1)
            (y, y_s) = f(len-2)
            if x > y + a[len-1]:
                res[len] = (x, x_s)
            else:
                n = list(y_s)
                n.append(a[len-1])
                res[len] = (y + a[len-1], n)
        return res[len]
    return f(len(a))


def max_wis2(a):
    x = (0, [])
    y = (0, [])
    for i in range(0, len(a)):
        temp = x
        if x[0] < y[0] + a[i]:
            n = list(y[1])
            n.append(a[i])
            x = (y[0] + a[i], n)
        y = temp

    
    return x




if __name__ == '__main__':
    arr = [7,2, 1, 8,6]
    print(max_wis(arr))
    print(max_wis2(arr))
    arr=[-1,-8,-10]
    print(max_wis(arr))
    print(max_wis2(arr))
    arr=[]
    print(max_wis(arr))
    print(max_wis2(arr))




