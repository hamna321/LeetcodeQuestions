class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mp = {0:1}
        for n in nums:
            temp = {}
            for s in mp.keys():
                temp[s+n] = temp[s+n] + mp[s] if s+n in temp else mp[s]
                temp[s-n] = temp[s-n] + mp[s] if s-n in temp else mp[s]
            mp = temp
        return mp[target] if target in mp else 0