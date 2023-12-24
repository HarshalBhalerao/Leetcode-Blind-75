class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We will tackle this by using 2 pointers
        l, r = 0, 1
        maxProfit = 0 # Keep track of the max profit

        # while our right pointer does not reach the end of the array
        while r < len(prices):
            # if price of left pointer is less than right pointer, calculate maxProfit
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(profit, maxProfit)
            else:
                l = r # if r pointer price is less than left pointer than set left position to right

            r += 1 #Increment right pointer

        return maxProfit

