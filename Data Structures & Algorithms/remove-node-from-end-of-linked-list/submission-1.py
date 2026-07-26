# Definition for singly-linked list.


# corner cases
#  - empty list 
#  - one node
#  - two node 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# use dummy node 
# dont assume that head is dummy node 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        slow = dummy 
        fast = head
        
        i = 0
        while i < n and fast:
            fast = fast.next
            i+=1
        
        while fast:

            fast = fast.next         
            slow = slow.next

        # if slow and slow.next:
        slow.next = slow.next.next 
        
        return dummy.next