class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        lo = max(nums) #the lowest possible maxsum of a subarray 
        hi = sum(nums) #the highest possible maxsum of a subarray
        
        #binary search
        
        while lo < hi:
            mid = (lo + hi) // 2
            tmpsum = 0
            count = 1
            for num in nums:
                tmpsum += num
                if tmpsum > mid:
                    tmpsum = num
                    count += 1
            if count > m:
                lo = mid + 1
            else:
                hi = mid
        return lo