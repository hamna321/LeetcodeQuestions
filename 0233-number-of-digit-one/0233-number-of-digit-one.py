class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        multiplier = 1
        while multiplier <= n:
            divider = multiplier * 10
            count += (n // divider) * multiplier
            count += min(max(n % divider - multiplier + 1, 0), multiplier)
            multiplier *= 10
        return count
        