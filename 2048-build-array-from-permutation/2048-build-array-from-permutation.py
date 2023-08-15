class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        a  = len(nums)
        for i in range(a):
            ans.append(nums[nums[i]])
        return ans