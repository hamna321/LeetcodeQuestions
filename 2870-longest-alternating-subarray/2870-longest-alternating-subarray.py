class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        max_length = -1  # Initially assume no valid subarray exists
        current_length = 1  # Start with subarray length 1

        for i in range(1, len(nums)):
            # Check if nums[i] continues the alternating pattern
            if nums[i] - nums[i - 1] == (1 if current_length % 2 == 1 else -1):
                current_length += 1  # Increase the length of the current subarray
            else:
                # Reset if the pattern breaks, check if nums[i] can start a new pattern
                if nums[i] - nums[i - 1] == 1:
                    current_length = 2  # Start a new subarray with length 2
                else:
                    current_length = 1  # Otherwise, reset to 1
                
            # Update the maximum length if the current subarray is valid (length > 1)
            if current_length > 1:
                max_length = max(max_length, current_length)

        return max_length
