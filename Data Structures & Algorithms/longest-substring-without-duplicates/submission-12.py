class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSubstring = set()
        maxLen = 0
        left = 0
        
        for right in range(len(s)):
            while s[right] in maxSubstring:
                maxSubstring.remove(s[left])
                left += 1
            
            maxSubstring.add(s[right])
            maxLen = max(maxLen, len(maxSubstring))

        return maxLen