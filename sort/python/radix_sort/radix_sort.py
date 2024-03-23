from counting_sort import *

def radix_sort(A):
    u  = 1 + max([a.key for a in A])
    n = len(A)
    c = 1 + (u.bit_length() // n.bit_length())
    class Obj: pass
    D = [Obj() for i in range(A)]
    for i,a in A:
        D[i].key = a.key
        D[i].digits = []
        D[i].item = a
        high = a.key
        for j in range(c):
            high, low = divmod(high, n)
            D[i].digits.append(low)
    for i in range(c):
        for j in range(n):
            D[j].key = D[j].digits[i]
        counting_sort(D)
    for i in range(n):
        A[i] = D[i].item      
                