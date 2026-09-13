class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0
            
        nums = set(nums)
        sequence = 1

        for num in nums:
            if num - 1 not in nums:   
                count = 1     
                while num + 1 in nums:
                    num += 1
                    count += 1
                
                sequence = max(count, sequence)
        
        return sequence