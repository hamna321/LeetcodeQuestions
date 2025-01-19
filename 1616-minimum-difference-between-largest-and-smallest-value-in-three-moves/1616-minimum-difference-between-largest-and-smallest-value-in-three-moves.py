class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # First, sort the array to easily access smallest and largest values
        nums.sort()

        # Handle edge case when there are 4 or fewer numbers
        if len(nums) <= 4:
            return 0

        # Set the minimum difference initially to infinity
        min_difference = float('inf')

        # We will look at four cases after adjusting at most 3 elements
        # We are minimizing the difference by choosing the appropriate numbers to change
        # To optimize the result, there are four scenarios (removing the smallest/largest elements):
        
        # Remove 3 smallest, i.e. we will compare nums[-1] with nums[3]
        min_difference = min(min_difference, nums[-1] - nums[3])
        
        # Remove 3 largest, i.e. we will compare nums[-4] with nums[0]
        min_difference = min(min_difference, nums[-4] - nums[0])
        
        # Remove 2 smallest and 1 largest, i.e. compare nums[-2] with nums[2]
        min_difference = min(min_difference, nums[-2] - nums[2])
        
        # Remove 1 smallest and 2 largest, i.e. compare nums[-3] with nums[1]
        min_difference = min(min_difference, nums[-3] - nums[1])

        # Finally, return the minimum difference
        return min_difference
