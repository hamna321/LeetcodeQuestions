# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):

        if not(head and head.next): return head 

        newHead = head.next
        head.next, newHead.next = self.swapPairs(head.next.next), head

        return newHead
