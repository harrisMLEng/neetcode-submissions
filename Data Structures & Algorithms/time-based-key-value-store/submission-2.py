class TimeMap:

    def __init__(self):
        self.valueMap : dict[str, list[tuple[int, str]]] = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.valueMap[key].append((value, timestamp))
    

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        values = self.valueMap[key]

        l = 0
        r = len(values) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if timestamp >= values[m][1]:
                res = values[m][0]
                l = m + 1

            else:
                r = m-1

        return res





        
