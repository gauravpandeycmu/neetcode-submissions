class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        val = 0
        rightMax = [0] * len(prices)

        for i in range(len(prices)-1, -1, -1):
            rightMax[i] = val
            val = max(val, prices[i])
        print(rightMax)
        
        for i, ele in enumerate(prices):
            res = max(res, rightMax[i]-ele)
        return res