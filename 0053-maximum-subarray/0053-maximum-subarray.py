class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms = float('-inf')
        cs = 0

        for num in nums:
            cs = max(num, cs + num)
            ms = max(ms, cs )
        return ms
        