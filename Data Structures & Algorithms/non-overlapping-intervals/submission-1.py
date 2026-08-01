class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        min_interval = 0
        intervals.sort(key = lambda i : i[1])

        largest_interval = intervals[0]

        count = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < largest_interval[1]:
                count+=1
            else: 
                largest_interval = intervals[i]
        return count 
