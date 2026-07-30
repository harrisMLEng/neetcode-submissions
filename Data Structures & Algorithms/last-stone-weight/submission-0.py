class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [0] * len(stones)
        for i in range(len(stones)):
            heap[i] = -stones[i]

        heapq.heapify(heap)
        
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                diff = stone1-stone2
                heapq.heappush(heap, -diff)
        
        return -heap[0] if heap else 0


        