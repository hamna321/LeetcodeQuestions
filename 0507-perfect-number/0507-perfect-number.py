class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        perfect = [6,28,496,8128,33550336]
        return True if  num in perfect else False
