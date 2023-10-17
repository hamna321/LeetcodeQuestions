class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)  # string length
        L = len(words)  # total words
        if L == 0:
            return []
        w = len(words[0])  # word length
        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1
        ans = []
        
        for i in range(w):
            l = i
            r = i
            cur_count = defaultdict(int)
            while r + w <= n:
                word = s[r:r + w]
                r += w
                if word in word_count:
                    cur_count[word] += 1
                    while cur_count[word] > word_count[word]:
                        cur_count[s[l:l + w]] -= 1
                        l += w
                    if r - l == L * w:
                        ans.append(l)
                else:
                    l = r
                    cur_count.clear()
        return ans