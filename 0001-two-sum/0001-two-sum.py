class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_indices = sorted(range(len(nums)), key=lambda k: nums[k])
        l = 0
        r = len(nums) - 1
        
        while l < r:
            current_sum = nums[sorted_indices[l]] + nums[sorted_indices[r]]
            
            if current_sum == target:
                return [sorted_indices[l], sorted_indices[r]]
            elif current_sum < target:
                l += 1
            else:
                r -= 1
        
        return []
