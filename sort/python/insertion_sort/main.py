import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'sort_util')))

import sort_util

def insertion_sort(A, i = None):
    if i == None: i = len(A) -1
    if i > 0:
        insertion_sort(A, i-1)
        insert_last(A,i)
    
def insert_last(A,i):
       if i > 0 and A[i] < A[i-1]:
            A[i], A[i-1] = A[i-1], A[i]
            insert_last(A, i-1)
            
            
def main():
    A = [1,5,3,4,7,1,7,11,6]
    insertion_sort(A)
    sort_util.is_sorted(A, lambda i,j: A[i] < A[j] )

main()    