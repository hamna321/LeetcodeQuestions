class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # approach 1
        count_0 ,result = 0,0
        for i in range(len(nums)):
            if nums[i] == 0:
                count_0 +=1
            else:
                count_0 = 0
            result += count_0
        return result