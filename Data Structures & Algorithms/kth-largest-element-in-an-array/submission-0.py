class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        largest = 0
        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap, -nums[i])

        for i in range(k):
            largest = -heapq.heappop(heap)

        return largest
        