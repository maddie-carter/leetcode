class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        smallest = float('inf')
        for price in prices:
            if price < smallest:
                smallest = price
            elif price - smallest > max_profit:
                max_profit = price - smallest
        return max_profit

# Test the function
if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    result = sol.maxProfit(prices)
    print("Result:", result)