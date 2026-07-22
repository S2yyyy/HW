# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        pre,cur=None,slow
        while cur:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
        while pre:
            if head.val!=pre.val:
                return False
            pre=pre.next
            head=head.next
        return True
