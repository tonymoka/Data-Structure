#      a
#    /   \
#   b     c
#  / \      \
# d   e      f
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def BredthFirst(root, target):
    q = [root]
    val=[]
    count = 0
    while(len(q) > 0):
        curr = q.pop(0)
        if curr.val == target:
            return True
        #print(curr.val)
        if curr.left != None:
            q.append(curr.left)
        if curr.right != None:
            q.append(curr.right)
    return False

# Driver Code:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
a.left = b
a.right = c
b.left = d
b.right = e
c.left = None
c.right = f

# head = a
# q = []
# while(head != None):
#     q.append(head.left)
#     q.append(head.right)
#     head = head.left

print(BredthFirst(a,'z'))