class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []

        sort = []

        for i in range(len(position)):
            sort.append((position[i], speed[i]))

        sort.sort(key=lambda x: x[0], reverse=True)

        for pos,speed in sort:
            stack.append((target - pos) / speed)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


        






        