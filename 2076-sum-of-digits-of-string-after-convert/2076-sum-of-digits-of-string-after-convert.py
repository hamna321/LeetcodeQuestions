class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Correct alphabet mapping (1-based index)
        alphabet_value = {
            'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 
            'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
            'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
            'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
            'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
            'z': 26
        }
        
        # Step 1: Convert string to numerical representation
        num_str = ''
        for char in s:
            num_str += str(alphabet_value[char])
        
        # Step 2: Transform k times
        for _ in range(k):
            total = 0
            for digit in num_str:
                total += int(digit)
            num_str = str(total)
        
        return int(num_str)