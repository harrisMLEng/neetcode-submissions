class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort(key=lambda i : i[0])

        newInterval = intervals[0]

        for i in range(1, len(intervals)):
            
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                newInterval = intervals[i]
            else:
                newInterval[0]=min(intervals[i][0], newInterval[0])
                newInterval[1]=max(intervals[i][1], newInterval[1])

        res.append(newInterval)
        return res



        
        