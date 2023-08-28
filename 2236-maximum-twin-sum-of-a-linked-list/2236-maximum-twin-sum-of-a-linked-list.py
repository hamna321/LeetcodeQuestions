# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        curr = head
        value = []

        while curr:
            value.append(curr.val)
            curr = curr.next
        
        i = 0
        j = len(value) - 1
        maxSum = 0
        while(i < j):
            maxSum = max(maxSum, value[i] + value[j])
            i += 1
            j -= 1
        
        return maxSum