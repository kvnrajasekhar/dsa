#Link : https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next= head   # dummy -> head ->  
        prev, curr = dummy,head
        while curr and curr.next:
            carry = ""
            curr.val = curr.val * 2
            if len(str(curr.val)) > 1:
                carry = (str(curr.val))[0]
                prev.val += int(carry)
                curr.val = int((str(curr.val))[1])
            curr = curr.next
            prev=prev.next
        curr.val = curr.val * 2
        if len(str(curr.val)) > 1:
            carry = (str(curr.val))[0]
            prev.val += int(carry)
            curr.val = int((str(curr.val))[1])
        if dummy.val >0:
            return dummy
        else :
            return dummy.next


        
