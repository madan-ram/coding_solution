# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        
        if(l1==None):
            return l2
        if(l2==None):
            return l1
        root1=l1
        while(l2!=None):
            l1=root1
            prevRoot=None
            while(l1!=None and l2.val>=l1.val):
                prevRoot=l1
                l1=l1.next
            if(prevRoot==None):
                temp=l2.next
                l2.next=root1
                root1=l2
                l2=temp
            else:
                temp=l2.next
                prevRoot.next=l2
                prevRoot.next.next=l1
                l2=temp
        l1=root1
        return l1
                
s=Solution()
l1=ListNode(5)
l2=ListNode(1)
l2.next=ListNode(2)
l2.next.next=ListNode(4)
res=s.mergeTwoLists(l1,l2)
while(res!=None):
    print res.val
    res=res.next