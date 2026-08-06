class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = defaultdict(list)
        for ana in strs:
            a=''.join(sorted(ana))
            anagrams[a] = []
        for char in strs:
            a=''.join(sorted(char))
            if a in anagrams:
                anagrams[a].append(char)
        
        for k,v in anagrams.items():
            result.append(v)


        return result


        
        