class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: 
            return 0

        nums = sorted(set(nums))
        max_sequence = 1
        max_sequences = []

        for i in range(len(nums)):
            if (i != (len(nums) - 1)) and nums[i + 1] == nums[i] + 1:
                max_sequence += 1
            
            else:
                max_sequences.append(max_sequence)
                max_sequence = 1

        return max(max_sequences)