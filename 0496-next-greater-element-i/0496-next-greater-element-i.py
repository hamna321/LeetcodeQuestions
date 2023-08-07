class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
        def test(n2,n):
            for x in n2:
                if x > n:
                    return x
            return -1

        return [ test(nums[nums.index(n)+1:],n) for n in findNums ]