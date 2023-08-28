# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, h):

        if not(h and h.next): return h 
# new head    # h = head       
        NH = h.next
        h.next, NH.next = self.swapPairs(h.next.next), h

        return NH
