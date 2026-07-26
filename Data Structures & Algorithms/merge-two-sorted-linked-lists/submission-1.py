# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a new list 
        list3 = curr = ListNode(-1)

        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val < curr2.val:
                newNode = ListNode(curr1.val)
                curr.next = newNode
                curr = curr.next
                curr1 = curr1.next
            elif curr2.val < curr1.val:
                newNode = ListNode(curr2.val)
                curr.next = newNode
                curr = curr.next
                curr2 = curr2.next
            else:
                newNode = ListNode(curr2.val)
                curr.next = newNode
                curr = curr.next
                newNode = ListNode(curr1.val)
                curr.next = newNode
                curr = curr.next

                curr1 = curr1.next
                curr2 = curr2.next

        while curr1:
            newNode = ListNode(curr1.val)
            curr.next = newNode
            curr = curr.next
            curr1 = curr1.next

        while curr2:
            newNode = ListNode(curr2.val)
            curr.next = newNode
            curr = curr.next
            curr2 = curr2.next

        
        return list3.next

                
