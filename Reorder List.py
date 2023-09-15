# problem link : https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first we will make the list into two halfs and we go from start in 1st half and we #will move from end in second half and replace the last ele to the second ele in the ist half
        first , second = head , head.next
        while second and second.next:# to make list two halfs
            first=first.next
            second=second.next.next 
        #next we will reverse second half list
        secondhalf = first.next
        prev = first.next= None
        while secondhalf:
            temp=secondhalf.next
            secondhalf.next=prev
            prev=secondhalf
            secondhalf=temp
        firsthalf , secondhalf = head,prev
        # combining the two lists for result
        while secondhalf:
            temp1 , temp2=firsthalf.next,secondhalf.next
            firsthalf.next=secondhalf
            secondhalf.next=temp1
            firsthalf,secondhalf=temp1,temp2
