from typing import List

class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()

        maximum_value = nums[-1]
        minimum_value = nums[0]

        result = maximum_value - minimum_value
        
        for i in range(1, len(nums)):
            max_value = max(maximum_value - k, nums[i - 1] + k)
            min_value = min(minimum_value + k, nums[i] - k)
            result = min(result, max_value - min_value)

        return result
