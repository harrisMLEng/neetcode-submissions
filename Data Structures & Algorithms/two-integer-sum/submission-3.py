class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i,num in enumerate(nums):
            cache[num] = i

        for i,num in enumerate(nums):
            if target - num in cache and i != cache[target - num]:
                return [i, cache[target - num]]

        return [] 

        