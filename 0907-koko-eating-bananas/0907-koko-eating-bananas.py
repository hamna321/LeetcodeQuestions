class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right, left = max(piles), 1
        while left < right:
            middle = (left + right) // 2
            count = 0
            for each in piles:
                count += ceil(each / middle)
            if count > h:
                left = middle + 1
            else:
                right = middle
        return left