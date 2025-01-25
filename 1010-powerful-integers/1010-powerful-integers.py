from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = []
        end = 20  # A reasonable assumption; max iterations if x or y is large.
        for i in range(end):
            for j in range(end):
                element = (x ** i) + (y ** j)
                if element > bound:
                    break
                res.append(element)
        
        return list(set(res))  # Use `set` to avoid duplicates.
