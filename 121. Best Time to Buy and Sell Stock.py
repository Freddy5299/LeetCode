# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
#
# 注意：你不能在买入股票前卖出股票。
from typing import List
class Solution:
    def maxProfit(self, prices: 'List[int]') -> int:
        profit = 0
        mixPrice = float('inf')
        if prices in []:
            return 0
        for price in prices:
            if price < mixPrice :
                mixPrice = price
            elif price-mixPrice>profit:
                profit = price-mixPrice
        return profit
    def maxProfitMy(self,prices:List[int]) -> int:
        n = len(prices)
        if n<=1: return 0
        listTemp = [1]*(n)
        listTemp[0] = 0
        for i in range(1,n):
            listTemp[i] = prices[i]-prices[i-1]
        for i in range(1,n):
            listTemp[i] = max(listTemp[i],listTemp[i-1]+listTemp[i])
        return max(listTemp)

if __name__ == '__main__':
    list = []
    s = Solution()
    print(s.maxProfitMy(list))