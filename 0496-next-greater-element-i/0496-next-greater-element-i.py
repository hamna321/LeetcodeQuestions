class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        
        def test(n2,n):
            for i in n2:
                if i > n:
                    return i
            return -1

        return [ test(nums[nums.index(n)+1:],n) for n in findNums ]
#For n = 4:
# The index of 4 in nums is 2.
# get the sub-list of elements after the index of 4 in nums: [2].
# Call the test function with the sub-list [2] and n = 4. Since there is no element greater than 4 in [2], the result is -1.