from typing import List

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        freq = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                next_num = nums[i + 1]
                freq[next_num] = freq.get(next_num, 0) + 1
        
        # Find number with max frequency
        max_count = 0
        result = -1
        for num, count in freq.items():
            if count > max_count:
                max_count = count
                result = num
        
        return result
