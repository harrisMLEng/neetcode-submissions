class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cache = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in cache:
                count = 1
                while num in cache:
                    if num + 1 in cache:
                        cache.remove(num)
                        count+=1
                        num +=1
                    else:
                        cache.remove(num)
                longest = max(longest, count)
        return longest