class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i, v in enumerate(nums):
            
            if v > 0 or i > len(nums) - 3:
                break

            elif i > 0 and v == nums[i - 1]:
                continue
            
            else:
                left, right = i + 1, len(nums) - 1
                target = 0 - v

                # Two sum
                while left < right:
                    if nums[left] + nums[right] == target:
                        result.append([nums[left], v, nums[right]])
                        left += 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
                            
                    elif nums[left] + nums[right] > target:
                        right -= 1

                    else:
                        left += 1

        return result