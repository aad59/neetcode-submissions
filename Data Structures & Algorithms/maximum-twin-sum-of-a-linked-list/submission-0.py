# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        rev = None
        slow = head
        fast = head

        while fast and fast.next:
            if not rev:
                rev = ListNode(slow.val)
            else:
                rev = ListNode(slow.val, rev)
            slow = slow.next
            fast = fast.next.next

        myMax = 0
        while slow:
            myMax = max(slow.val + rev.val, myMax)
            slow = slow.next
            rev = rev.next

        return myMax
            