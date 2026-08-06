class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        output = []
        heap = []

        for num in nums:
            count[num] += 1

        for key,v in count.items():
            heapq.heappush(heap, (-v,key))
        
        for i in range(k):
            output.append(heapq.heappop(heap)[1])

        return output


        