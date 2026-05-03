# Last updated: 04/05/2026, 00:34:02
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum=0
        carry=0
        result=ListNode()
        result.val="Start"
        result.next=None
        temp=result
        
        while l1 != None and l2 != None:
            sum=l1.val + l2.val+carry
            r=sum%10
            current=ListNode()
            current.val=r
            temp.next=current
            temp=current

            if(sum>=10):
                carry=1
            else:
                carry=0
            l1=l1.next
            l2=l2.next
        if(l1==None and l2 != None):
            while l2 != None:
                sum=l2.val+carry
                r=sum%10
                current=ListNode()
                current.val=r
                temp.next=current
                temp=current

                if(sum>=10):
                    carry=1
                else:
                    carry=0            
                l2=l2.next
        if(l2==None and l1 != None):
            while l1 != None:
                sum=l1.val+carry
                r=sum%10
                current=ListNode()
                current.val=r
                temp.next=current
                temp=current

                if(sum>=10):
                    carry=1
                else:
                    carry=0
                l1=l1.next


        if(carry>0):
            current=ListNode()
            current.val=carry
            temp.next=current
            
        return result.next
            
        