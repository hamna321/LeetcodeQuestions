class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        dic = {}  
        max_char = 1 
        
      
        words = sentence.split()
        
        for word in words:
            
            dic[max_char] = word
            
            if word.startswith(searchWord):
                return max_char
            
            max_char += 1 
        

        return -1