# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        #   1 0 1  (2) -> decimal  1 2 ^ 0 
        #  1 * 2 + 0 -> 2 * 2 + 1 
        # res = result
        res = head.val
        while head.next:
            res = res * 2 + head.next.val
            head = head.next

        return res