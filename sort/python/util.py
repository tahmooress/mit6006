def is_sorted(A,predicate):
    for i in range(A.length-2):
        if not predicate(A[i], A[i+1]) :
            return False
    return True    