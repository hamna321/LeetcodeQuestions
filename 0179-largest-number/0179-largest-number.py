from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def comp(a, b):
            ab = a + b
            ba = b + a
            if ab > ba: return -1
            if ba > ab: return 1
            return 0

        nums_s = sorted([str(v) for v in nums], key=cmp_to_key(comp))
        return "0" if nums_s[0] == "0" else "".join(nums_s)