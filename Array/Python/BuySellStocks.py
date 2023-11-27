class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for i,price in enumerate(prices[1:]):
            max_profit = max(max_profit,price-min_price)
            min_price = min(min_price,price)
        return max_profit
    
mySol = Solution()
print(mySol.maxProfit([7,1,5,3,6,4]))
print(mySol.maxProfit([7,6,4,3,1]))
