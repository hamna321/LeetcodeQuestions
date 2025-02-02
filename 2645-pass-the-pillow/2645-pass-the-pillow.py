class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        index = 0
        direction = 1  
        
        for t in range(time):
            index += direction 
            
            
            if index == n - 1 or index == 0:
                direction *= -1  

        return index + 1  
