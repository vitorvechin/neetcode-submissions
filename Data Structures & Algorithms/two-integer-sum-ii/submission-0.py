class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1

        for i in range(n):
            sum = numbers[left] + numbers[right]

            if sum == target:
                return [left + 1, right + 1]
            
            elif sum > target:
                right -= 1
            
            else:
                left += 1
        
