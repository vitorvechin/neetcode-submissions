class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        else:
            charCount = {}
            for i in range(len(s)):
                charCount[s[i]] = charCount.get(s[i], 0)
                charCount[s[i]] += 1

                charCount[t[i]] = charCount.get(t[i], 0)
                charCount[t[i]] -= 1

            return all(v == 0 for v in charCount.values())