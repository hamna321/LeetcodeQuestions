class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_height = 0
        sum = 0
        for i in range(len(gain)):
            sum += gain[i]
            max_height = max(max_height, sum)
        return max_height
        