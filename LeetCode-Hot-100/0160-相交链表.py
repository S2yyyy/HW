# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p,q=headA,headB
        while p is not q:
            p = p.next if p is not None else headB
            q = q.next if q is not None else headA
        return p
