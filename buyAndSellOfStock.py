class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        left=0
        right=1
        while(right<len(prices)):
            profit=prices[right]-prices[left]
            if prices[left]<prices[right]:
                maxProfit=max(maxProfit,profit)
            else:
                left=right
            right+=1
        return maxProfit
            
