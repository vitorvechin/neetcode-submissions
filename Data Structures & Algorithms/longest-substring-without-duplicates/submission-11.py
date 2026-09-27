class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        else:
            left = 0
            right = 1
            maxSubstring = set(s[left])
            maxLen = 1

            while right < len(s):
                if s[right] not in maxSubstring:
                    maxSubstring.add(s[right])
                    maxLen = max(maxLen, len(maxSubstring))
                    right += 1
                
                else:
                    while s[left] != s[right]:
                        maxSubstring.remove(s[left])
                        left += 1
                    
                    left += 1
                    right += 1

        return maxLen
