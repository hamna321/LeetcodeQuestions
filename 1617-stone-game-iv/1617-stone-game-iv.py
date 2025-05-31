class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {}

        def can_win(k):
            if k in memo:
                return memo[k]
            i = 1
            while i * i <= k:
                if not can_win(k - i * i):
                    memo[k] = True
                    return True
                i += 1
            memo[k] = False
            return False

        return can_win(n)
