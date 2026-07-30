class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [0] * len(nums) 
        for i in range(len(nums)):
            self.heap[i] = -nums[i]

        heapq.heapify(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        largest = 0
        temp = []
        for i in range(self.k):
            largest = -heapq.heappop(self.heap)
            temp.append(largest)
        for i in range(len(temp)):
            heapq.heappush(self.heap, -temp[i])
        
        return largest

        

