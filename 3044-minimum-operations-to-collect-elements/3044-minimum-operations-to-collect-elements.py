class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        Minimum_operator = 0
        collected = set()

        for num in reversed(nums):

            Minimum_operator += 1

            if 1 <= num <= k:
                collected.add(num)
                
            if len(collected) == k:
                break

        return Minimum_operator

