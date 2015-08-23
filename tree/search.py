class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def isPresent (a , b):
    while(a!=None):
        if a.value==b:
            return 1
        elif a.value<b:
            a=a.right
        else:
            a=a.left
    return 0

t1=TreeNode(20)
t1.left=TreeNode(10)
t1.left.right=TreeNode(12)
t1.left.left=TreeNode(10)
t1.right=TreeNode(30)
t1.right.left=TreeNode(25)
t1.right.right=TreeNode(40)
print isPresent(t1,10)
print isPresent(t1,81)