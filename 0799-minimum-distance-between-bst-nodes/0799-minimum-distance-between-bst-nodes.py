# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        prev = None
        minDiff = float('inf')
        
        def inorder(node):
            nonlocal prev, minDiff
            if not node:
                return
            inorder(node.left)
            if prev:
                minDiff = min(minDiff, node.val - prev.val)
            prev = node
            inorder(node.right)
        
        inorder(root)
        return minDiff
        