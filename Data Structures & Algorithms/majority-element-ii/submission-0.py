class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        numb=[]
        for num in nums:
            count[num] = 1 + count.get(num,0)
        print(count)
        for key,value in count.items():
            if value > len(nums)/3:
                numb.append(key)
        return numb
        