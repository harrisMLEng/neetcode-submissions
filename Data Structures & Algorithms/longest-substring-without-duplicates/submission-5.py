class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = set()
        length = 0
        count = 0
        l = 0
        for r, char in enumerate(s):
            while l < r and char in cache:
                cache.remove(s[l])
                l+=1
                count -= 1

            cache.add(char)
            count += 1

            length = max(length, count)
        return length
        

         