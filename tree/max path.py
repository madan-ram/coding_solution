# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    maxi = 0
    def __maxDepth__(self, root, pathCount):
        if root == None:
            if self.maxi < pathCount:
                self.maxi = pathCount
            return self.maxi
        
        self.__maxDepth__(root.left, pathCount+1)
        self.__maxDepth__(root.right, pathCount+1)
        return self.maxi

    def maxDepth(self, root):
        result = self.__maxDepth__(root, 0)
        return result
        
t=TreeNode("A")
t.left=TreeNode("B")
t.left.right=TreeNode("E")
t.right=TreeNode("C")
t.right.left=TreeNode("D")
s=Solution()
print s.maxDepth(t)