class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        from collections import defaultdict
        
        count = defaultdict(int)
        left = 0
        max_length = 0

        for right in range(len(s)):
            count[s[right]] += 1

            while count[s[right]] > 2:
                count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
