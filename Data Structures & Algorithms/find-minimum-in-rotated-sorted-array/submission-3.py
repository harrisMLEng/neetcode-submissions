class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minVal = nums[l] if nums[l] < nums[r] else nums[r]
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] < nums[r]:
                r = m
            else:
                l = m+1 #rotation search right
            
            minVal = min(nums[m], minVal)
        return minVal

            



        