xs = [64, 25, 12, 22, 11]

def select_sort(xs):
    for i in range(0, len(xs)-1):
        minimum = i
        for j in range(i+1, len(xs)):
            if xs[j] < xs[minimum]:
                minimum = j

        if minimum != i:
            xs[minimum], xs[i] = xs[i], xs[minimum]
    return xs
print(select_sort(xs))