class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,v in enumerate(s):
            if s.count(v)==1:
               return i
               break 
        return -1
