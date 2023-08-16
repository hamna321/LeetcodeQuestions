class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Fermat theorem on sum of two squares
        x = 2
        while x*x <= c: 
            if c % x == 0: 
                mult = 0
                while c % x == 0: 
                    mult += 1
                    c //= x
                if x % 4 == 3 and mult & 1: return False 
            x += 1
        return c % 4 != 3