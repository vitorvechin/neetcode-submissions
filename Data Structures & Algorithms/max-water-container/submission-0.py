class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(x1, x0, y1, y0):
            return (x1 - x0) * min(y1, y0)

        maxA = 0 
        left = 0
        right = len(heights) - 1
        
        while left != right:

            maxA = max(maxA, area(right, left, heights[right], heights[left]))

            if heights[left] < heights[right]:
                left += 1
            
            else:
                right -= 1

        return maxA