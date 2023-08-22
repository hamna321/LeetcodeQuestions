class Solution:
    def countVowels(self, word: str) -> int:
        dics = {'a':1,'e':1,'i':1,'o':1,'u':1}
        c ,l = 0,len(word)
        for i in range(l):
            if word[i] in dics:
                c += (l-i)*(i+1)
        return c