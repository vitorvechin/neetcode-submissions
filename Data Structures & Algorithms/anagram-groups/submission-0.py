class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anDict = {}

        for s in strs:
            orderedS = sorted(s)
            orderedS = "".join(orderedS)
            anDict[orderedS] = anDict.get(orderedS, [])
            anDict[orderedS].append(s)

        return list(anDict.values())  