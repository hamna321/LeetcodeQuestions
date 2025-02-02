class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0
        for x in range(limit + 1):
            for y in range(limit + 1):
                for z in range(limit + 1):
                    res = x + y + z
                    if res == n:
                        count += 1
        return count