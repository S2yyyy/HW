# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is not None:
            return list2
        elif list1 is not None and list2 is None:
            return list1
        elif list1 is None and list2 is None:
            return None
        if list1.val<list2.val:
            head=list1
            list1=list1.next
        else:
            head=list2
            list2=list2.next
        pre=head
        while list1 and list2:
            if list1.val<list2.val:
                head.next=list1
                head=head.next
                list1=list1.next
            else:
                head.next=list2
                head=head.next
                list2=list2.next
        while list1:
            head.next=list1
            head=head.next
            list1=list1.next
        while list2:
            head.next=list2
            head=head.next
            list2=list2.next
        return pre
