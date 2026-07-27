class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # hashmap of s1

        # loop through s2 
        # first character found in hashmpa
        # start second loop

        hashmap = defaultdict(int)
        cache = set(s1)
        for s in s1:
            hashmap[s] += 1
        

        for r in range(len(s2)):
            if s2[r] in cache:
                substr = s2[r:r+len(s1)]
                if sorted(substr) == sorted(s1):
                    return True
                

        return False


        