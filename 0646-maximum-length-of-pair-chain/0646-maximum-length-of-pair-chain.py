class Solution:
    def findLongestChain(self, pairs: list[list[int]]) -> int:

        a, c = 0, (-inf)
        pairs.sort(key = lambda x: x[1])

        for l, r in pairs:
            if l > c:
                a += 1
                c = r

        return  a

        # a = ans
        # c = chainend