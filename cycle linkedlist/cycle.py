#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        temp1=head
        temp2=head
        if temp1==None or temp2.next==None:
            return False
        while(temp2.next!=None and temp1.next!=None and temp2.next.next!=None):
            temp1=temp1.next
            temp2=temp2.next.next
            if(temp1==temp2):
                return True
        return False
s=Solution()
l1=ListNode(10)
l1.next=ListNode(20)
l1.next.next=ListNode(30)
l1.next.next.next=l1
print s.hasCycle(l1)
l1=ListNode(10)
l1.next=ListNode(20)
l1.next.next=ListNode(30)
print s.hasCycle(l1)
l1=None
print s.hasCycle(l1)