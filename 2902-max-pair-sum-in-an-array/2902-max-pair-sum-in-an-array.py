class Solution:
    def maxSum(self, nums: List[int]) -> int:
        mbd = defaultdict(int)
        ms = -1

        for num in nums:
            d = max(str(num))

            if d in mbd:
                ms = max(ms, mbd[d] + num)

            mbd[d] = max(mbd[d], num)

        return ms

        # mbd max_by_digit
        # max_sum
        #d = digit