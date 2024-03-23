

def selection_sort(A, i = None):
    if i == None: i = len(A) -1
    if i > 0:
        j = find_max_prefix(A, i)
        A[i] , A[j] = A[j], A[i]
        selection_sort(A, i-1)
    
def find_max_prefix(A,i):
    if i > 0:  
        j = find_max_prefix(A, i -1)
        if A[i] < A[j]:
            return j
    return i    