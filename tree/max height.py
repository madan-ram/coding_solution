#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    count=0
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        depth=1
        count=0
        S=[]
        SLen=[]
        if root==None:
            return 0
        else:
            S.append(root)
            SLen.append(1)
        while(len(S[count:])>0):
            node=S[count]
            l=SLen[count]
            count=count+1
            if(node.left!=None):
                S.append(node.left)
                SLen.append(l+1)
                if depth<l+1:
                    depth=l+1
            if(node.right!=None):
                S.append(node.right)
                SLen.append(l+1)
                if depth<l+1:
                    depth=l+1
        return depth
            
t=TreeNode("A")
t.left=TreeNode("B")
t.left.right=TreeNode("E")
t.right=TreeNode("C")
t.right.left=TreeNode("D")
s=Solution()
print s.maxDepth(t)