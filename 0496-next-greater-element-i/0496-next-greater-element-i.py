class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
        def test(lst,n):
            for x in lst:
                if x > n:
                    return x
            return -1

        return [ test(nums[nums.index(n)+1:],n) for n in findNums ]