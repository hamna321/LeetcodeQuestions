class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        # Use a set for faster lookup of numbers in the list
        num_set = set(nums)
        
        # Start checking for the smallest power of two not present in num_set
        value = 1
        while value in num_set:
            value *= 2  # Move to the next power of two
        
        return value