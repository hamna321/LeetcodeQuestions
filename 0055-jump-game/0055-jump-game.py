class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = len(nums) - 1
        for r in range(len(nums)-1,-1,-1):
            if r + nums[r] >= l :  l = r 
        return l == 0