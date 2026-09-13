class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.lower())
        print(s)
        newS = []
        
        for c in s:
            if c.isalnum():
                newS.append(c)
        
        newS = "".join(newS)
        n = len(newS)
        print(newS)

        for i in range(n // 2):
            if newS[i] != newS[n - 1 - i]:
                return False
        
        return True