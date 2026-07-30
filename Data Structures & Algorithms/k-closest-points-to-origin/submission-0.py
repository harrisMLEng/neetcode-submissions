class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        res = []
        for i in range(len(points)):
            heapq.heappush(dist, (math.sqrt(points[i][0]**2 + points[i][1]**2), i))

        for i in range(k):
            index = heapq.heappop(dist)[1]
            res.append(points[index])

        return res

        
        

        