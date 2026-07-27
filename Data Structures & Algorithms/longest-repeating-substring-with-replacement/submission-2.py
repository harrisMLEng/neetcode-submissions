class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # take first character to replace or the most frequent one
        # loop thorugh s:
            # increament length
            # if char not in cache:
                # check k value
                # replace char with the one in cache/the most frequent one
                # 

            # add to cache
            # 
        l = 0 
        res = 0
        count = defaultdict(int)
        maxf = 0

        for r in range(len(s)):
            count[s[r]] += 1

            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res





        

        