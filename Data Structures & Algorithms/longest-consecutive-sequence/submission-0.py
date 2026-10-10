class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new = set(nums)
        res=0
        for num in nums:
            if (num-1) not in new:
                length=1
                while(num + length) in new:
                    length+=1
                res = max(res,length)
        return res
        