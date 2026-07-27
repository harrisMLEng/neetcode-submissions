class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        days = [0] * len(temperatures)
        stack = []
        for day,temp in enumerate(temperatures):

            while stack and temp > stack[-1][1]:
                past, tmp = stack.pop()
                diff = day - past
                days[past] = day - past
            stack.append((day, temp))
            
        return days


            
        