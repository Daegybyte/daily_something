"""
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
    
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Max_Profit:
    def __init__(self, prices: list = [7,1,5,3,6,4]) -> None:
        self.prices = prices
    
    def money_maker(self) -> int:
        if len(self.prices) < 2:
            return 0
        
        min_price = self.prices[0]
        max_profit = 0
        
        for price in self.prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, abs(min_price - price))
            
        return max_profit
            
        

if __name__ == '__main__':
    instance = Max_Profit()
    assert(instance.money_maker() == 5)
    
    instance = Max_Profit(prices=[7,6,4,3,1])
    assert(instance.money_maker() == 0)