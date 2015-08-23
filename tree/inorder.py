# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class stack:
    l=[]
    top=0
    size=0
    def __init__(self,size=100):
        self.size=size
        self.l=[0]*size
    
    def push(self,x):
        if self.isfull()!=True:
            self.l[self.top]=x
            self.top=self.top+1
        else:
            return None
        
    def pop(self):
        if self.isempty()!=True:
            val=self.l[self.top-1]
            self.top=self.top-1
            return val
        else:
            return None
        
    def isempty(self):
        if self.top==0:
            return True
        return False
        
    def isfull(self):
        if self.top>=self.size:
            return True
        return False
        
class Solution:
    l=[]
    # @param root, a tree node
    # @return a list of integers
    def __init__(self):
    	self.l=[]
    def inorderTraversal(self, root):
        st=stack()
        while(True):
            while root!=None:
                st.push(root)
                root=root.left
            
            if st.isempty():
                break
            root=st.pop()
            self.l.append(root.val)
            root=root.right
        return self.l

t1=TreeNode("A")
t1.left=TreeNode("B")
t1.left.right=TreeNode("E")
t1.right=TreeNode("C")
t1.right.left=TreeNode("D")
s=Solution()
print s.inorderTraversal(t1)

t1=TreeNode("1")
t1.left=TreeNode("2")
s=Solution()
print s.inorderTraversal(t1)

t1=None
t1=TreeNode("A")
s=Solution()
print s.inorderTraversal(t1)
t1=None
t1=TreeNode("A")
t1.left=TreeNode("B")
s=Solution()
print s.inorderTraversal(t1)
t1=None
s=Solution()
print s.inorderTraversal(t1)