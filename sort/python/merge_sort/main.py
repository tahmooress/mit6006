def merge_sort(A, a = 0, b = None):
    if b == None: b = len(A)
    if 1 < b - a:
        m = (a+b+1) // 2
        merge_sort(A, a, m)
        merge_sort(A, m, b)
        L, R = A[a:m], A[m:b]
        merge(A, L, R, len(L), len(R), a, b)
    
    
def merge(A, L, R, i, j, a, b):
     if a < b:
        if j <= 0 or (i > 0 and L[i -1] > R[j -1]):
            A[b - 1] = L[i - 1]
            i -= 1
        else:
            A[b - 1] = R[j - 1]
            j -= 1
        merge(A, L, R , i, j, a, b -1)

def merge_sort_inplace(A, a = 0, b = None):
    if b == None: b = len(A)
    if 1 < b - a:
        m = (a+b+1) // 2
        merge_sort(A, a, m)
        merge_sort(A, m, b)
        inplace_merge(A, a, m, b)
    

def inplace_merge(A, i, k, j):
    if j <= k: return
    if A[k - 1] >= A[j -1]:
        A[k - 1], A[j - 1] = A[j - 1], A[k - 1]
        for r in range(k -1, i , -1):
            if A[r] < A[r - 1]:
                A[r], A[r - 1] = A[r - 1] , A[r]                                                    
    inplace_merge(A, i, k, j -1)
        
def main():
    A = [1,5,3,2]    
    merge_sort(A)
    print(A)
    B = [1,5,3,2,6,4, 9, 7]
    merge_sort_inplace(B)
    print(B)
    
main()     