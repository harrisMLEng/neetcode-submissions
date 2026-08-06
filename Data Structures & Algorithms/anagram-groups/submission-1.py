class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for char in strs:
            a=''.join(sorted(char))
            anagrams[a].append(char)


        return list(anagrams.values())


        
        