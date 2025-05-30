class Solution:
    def winnerSquareGame(self, n: int) -> bool:
     
        memo = {}
        
        def can_win(k):
            
            if k in memo:
                return memo[k]
                
            
            root = int(k ** 0.5)
            if root * root == k:
                memo[k] = True
                return True
                
            
            if k == 1:
                memo[k] = True
                return True
            if k == 2:
                memo[k] = False
                return False
                
            
            for move in range(1, root + 1):
                square = move * move
                if square > k:
                    break
                if not can_win(k - square):
                    memo[k] = True
                    return True
                    
            memo[k] = False
            return False
        
        return can_win(n)