class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a =  len(nums)
        count = 0
        j =  1
        for i in range(a):
            for j in range(a):
              if nums[i] == nums[j] and i < j:
                count += 1
        return count