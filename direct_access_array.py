class direct_access_array:
    def __init__(self, u):
        self.A = [None] * u
    def find(self, key):
       return self.A[key]
    def insert(self,x):        
        self.A[x.key] = x
    def delete(self,key):
        self.A[key] = None
    def find_next(self, key):
        for i in range(key,len(self.A)):
            if self.A[i] is not None:
                return self.A[i]    
    def find_max(self):
        for i in range (len(self.A), -1, -1, -1):
            if self.A[i] is not None:
                return self.A[i]
    def delete_max(self):
        k = self.find_max().key
        self.delete(k)
        return k
    
def mdiv(k, n):
    (a, b) = divmod(k,n)
    print(a,b)

def counting_sort(A):
    
    u = 1 + max([x.key for x in A])
    D = [0] * u
    for x in A:
            D[x.key] += 1
    for k in range(1, u):
        D[k]+=D[k-1]
    for x in list(reversed(A)):
            A[D[x.key] - 1] = x
            D[x.key] -= 1

A = [{"key": 1},{"key": 4},{"key": 1},{"key": 2},{"key": 5},{"key": 7},{"key": 2}]   

counting_sort(A)
print(A)
