class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxTillNow = 0
        res = 0

        for i in range(len(prices)-1, -1, -1):
            res = max(res, maxTillNow-prices[i])
            maxTillNow = max(maxTillNow, prices[i])
        return res