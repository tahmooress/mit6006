def counting_sort(A):
    u = 1 + max([a.key for a in A])
    D = [[] for i in range(u)]
    for x in A:
        D[x.key].append(x)
    i = 0
    for chian in D:
        for c in chian:
            A[i] = c
            i += 1
