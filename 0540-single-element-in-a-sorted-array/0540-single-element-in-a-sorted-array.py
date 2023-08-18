class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s=sum(nums)
        a=set(nums)
        l=list(a)
        o=sum(l)

        return (2*o-s)