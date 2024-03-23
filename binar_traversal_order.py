class Node:
    def __init__(self ,item: str):
        self.item = item
        self.left = None
        self.right = None

class NodeRoot():
    def __init__(self,node: Node):
        self.root = node

    def preorder_traversal(self):
        print("preorder_traversal:")
        self.__preorder_traversal__(self.root)
        print('')

    def __preorder_traversal__(self, root: Node):
        if not root: return
        self.__preorder_traversal__(root.left)
        self.__preorder_traversal__(root.right)
        print(root.item, end=' ')

    def inorder_traversal(self):
        print("inroder_traversal:")
        self.__inorder_traversal__(self.root)
        print('')

    def __inorder_traversal__(self, root: Node):
        if not root: return
        self.__inorder_traversal__(root.left)
        print(root.item, end=' ')
        self.__inorder_traversal__(root.right)

    def postorder_traversal(self):
        print("postorder_traversal:")
        self.__postorder_traversal(self.root)
        print('')

    def __postorder_traversal(self, root: Node):
        if not root: return
        print(root.item, end=' ')
        self.__postorder_traversal(root.left)
        self.__postorder_traversal(root.right)


    def construct(self, postorders: list, inorders: list):
        if len(inorders) == 1:
            if len(postorders) == 1:
                 postorders = []
            else: postorders =postorders[1:]       
            return Node(inorders[0])
        root_index = 0
        for i in range(len(inorders)):
            if inorders[i] == postorders[0]:
                root_index = i
        root = Node(postorders[0])
        root.left = self.construct(postorders[1:], inorders[:root_index])
        root.right = self.construct(postorders[1:], inorders[root_index + 1:])
        return root


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")
I = Node("I")
N = Node("N")
S = Node("S")
P = Node("P")
Q = Node("Q")



A.left = B
A.right = C
B.left = S
S.left = P
S.right= Q
B.right = D
D.right = N
C.left = E
E.left = G
C.right = F
F.left = H
F.right = I


root = NodeRoot(A)


root.preorder_traversal()
root.inorder_traversal()
root.postorder_traversal()


inorders = ["P", "S", "Q", "B", "D", "N", "A", "G", "E", "C", "H", "F", "I"]
postorders = ["A", "B", "S", "P", "Q", "D", "N", "C", "E", "G", "F", "H", "I"]

a = root.construct(postorders, inorders)

NodeRoot(a).inorder_traversal()