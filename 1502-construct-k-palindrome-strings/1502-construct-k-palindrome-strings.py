class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        dictionary = {}

        for char in s:
            dictionary[char] = dictionary.get(char, 0) + 1
        
        number = sum(1 for count in dictionary.values() if count % 2 != 0)
        
        if len(s) < k:
            return False
        if number <= k:
            return True
        
        return False
