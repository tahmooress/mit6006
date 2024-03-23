from sys import maxsize

def max_sub_array(A):
    sum = 0
    p,q, i,j = 0 , 0, 0, 0
    answer =  - (maxsize + 1)
    while i <len(A):
        sum += A[i]
        if answer < sum:
           answer = sum
           p, q = j, i
        if sum < 0:
            sum = 0 
            j = i +1 
        i +=1    
    return (p,q,answer)        
   
   
a = [-2, -3, 4, -1, -2, 1, 5, -3, -3, -9,17]
b = [-4, -2, -1,-6, -2]
print(max_sub_array(a))