class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        i = 0  
        
        for j in range(len(prices)):  
            if prices[j] < prices[i]:
                i = j
            else:
                if (prices[j] - prices[i]) > max:
                    max = prices[j] - prices[i]
                    
        return max