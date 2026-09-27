class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxProfit = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left += 1
                right = left + 1

            else:
                maxProfit = max(maxProfit, prices[right] - prices[left])
                right += 1
            
        return maxProfit