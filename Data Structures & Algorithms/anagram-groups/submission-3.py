class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            count = [0] * 26
            
            for i in range(len(s)):
                count[ord(s[i]) - 97] += 1
            
            count = tuple(count)
            anagrams[count] = anagrams.get(count, [])
            anagrams[count].append(s)
        
        return list(anagrams.values())
