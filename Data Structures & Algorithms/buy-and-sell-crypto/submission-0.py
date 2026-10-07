class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0 
        i = 0
        j = 1
        while j<len(prices):
            curr = prices[j] - prices[i]
            if curr>result:
                result = curr
            if prices[i]>prices[j]:
                i=j
                j+=1
            else:
                j+=1
        return result
        