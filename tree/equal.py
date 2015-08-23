#Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, root1, root2):
        eq=True
        count=0
        S1=[]
        S2=[]
        if root1==None and root2==None:
        	eq=True
        	return True
        	
        if (root1!=None and root2!=None) and (root1.val==root2.val):
            S1.append(root1)
            S2.append(root2)
        else:
        	return False
        	
        while(len(S1[count:])>0 and len(S2[count:])>0):
            node1=S1[count]
            node2=S2[count]
            count=count+1
            if(node1.left!=None and node2.left!=None):
                S1.append(node1.left)
                S2.append(node2.left)
                if node1.left.val!=node2.left.val:
                	eq=False
                	break
            elif not(node1.left==None and node2.left==None):
            	eq=False
            	break

            if(node1.right!=None and node2.right!=None):
                S1.append(node1.right)
                S2.append(node2.right)
                if node1.right.val!=node2.right.val:
                	eq=False
                	break
            elif not(node1.right==None and node2.right==None):
            	eq=False
            	break

        return eq
            
t1=TreeNode("A")
t1.left=TreeNode("B")
t1.left.right=TreeNode("E")
t1.right=TreeNode("C")
t1.right.left=TreeNode("D")

t2=TreeNode("A")
t2.left=TreeNode("B")
t2.left.right=TreeNode("E")
t2.right=TreeNode("C")
t2.right.left=TreeNode("D")

s=Solution()
print s.equal(t1,t2)