# base case
'''
n == 0 or n == 1 elif case n == 2
2 - else count for fibonacci using formula
F(n) = F(n - 1) + F(n - 2)
'''

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1 or n == 2: 
            return 1
        else:
            res = self.fib(n-1) + self.fib(n-2)

        return res
        

        

        