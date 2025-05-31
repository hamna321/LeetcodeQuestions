class Solution:
    def minOperations(self, s: str) -> int:
        count0 = 0  # changes if pattern starts with '0'
        count1 = 0  # changes if pattern starts with '1'
        
        for i, ch in enumerate(s):
            expected_char_0 = '0' if i % 2 == 0 else '1'
            expected_char_1 = '1' if i % 2 == 0 else '0'
            
            if ch != expected_char_0:
                count0 += 1
            if ch != expected_char_1:
                count1 += 1
        
        return min(count0, count1)
