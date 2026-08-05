class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # days = [0] * len(temperatures)
        # stack = []
        # for day,temp in enumerate(temperatures):

        #     while stack and temp > stack[-1][1]:
        #         past, tmp = stack.pop()
        #         diff = day - past
        #         days[past] = day - past
        #     stack.append((day, temp))
            
        # return days


        result = []

        for l in range(len(temperatures)):
            r = l + 1
            while r < len(temperatures):
                if temperatures[r] > temperatures[l]:
                    result.append(r - l)
                    break
                r += 1
            if r == len(temperatures):
                result.append(0)

        return result

                





















            
        