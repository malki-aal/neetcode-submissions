class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numb = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numb:
                return [numb[diff],i]
            numb[num]=i
        return none
        