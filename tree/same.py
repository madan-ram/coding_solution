class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def testEqual(self, p, q):
        if p.val == q.val:
            return True
        else:
            return False

    def isSameTree(self, p, q):
        if p == q:
            return True
        elif p == None and q!=None:
            return False
        elif q == None and p != None:
            return False
        else:
            return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left) and self.testEqual(p, q)

t = TreeNode("A")
t.left=TreeNode("B")
t.left.right=TreeNode("E")
t.right=TreeNode("C")
t.right.left=TreeNode("D")

t1 = TreeNode("A")
t1.left=TreeNode("B")
t1.left.right=TreeNode("E")
t1.right=TreeNode("C")


s=Solution()
print s.isSameTree(t,t1)

t = TreeNode("A")
t.left=TreeNode("B")
t.left.right=TreeNode("E")
t.right=TreeNode("C")
t.right.left=TreeNode("D")

t1 = TreeNode("A")
t1.left=TreeNode("B")
t1.left.right=TreeNode("E")
t1.right=TreeNode("C")
t1.right.left=TreeNode("D")

s=Solution()
print s.isSameTree(t,t1)


t = TreeNode("A")
t.left=TreeNode("B")
t.left.right=TreeNode("E")
t.right=TreeNode("C")
t.right.left=TreeNode("D")

t1 = None


s=Solution()
print s.isSameTree(t,t1)


t = None

t1 = None


s=Solution()
print s.isSameTree(t,t1)