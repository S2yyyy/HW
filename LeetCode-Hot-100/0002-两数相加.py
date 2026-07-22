# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1,num2=[],[]
        while l1:
            num1.append(str(l1.val))
            l1=l1.next
        while l2:
            num2.append(str(l2.val))
            l2=l2.next
        num1.reverse()
        num2.reverse()
        num1=int("".join(num1))
        num2=int("".join(num2))
        ans=num1+num2
        ans_pri=ListNode()
        tmp=ans_pri
        if ans==0:
            return tmp
        while ans!=0:
            num=ans%10
            ans=ans//10
            ans_cur=ListNode(val=num)
            ans_pri.next=ans_cur
            ans_pri=ans_pri.next
        return tmp.next
