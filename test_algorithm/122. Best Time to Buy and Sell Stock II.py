from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<=1:return 0
        listTemp = [0]*(n)
        for i in range(1,n):
            if (prices[i]-prices[i-1]) >0:
                listTemp[i] = prices[i]-prices[i-1]
        return sum(listTemp)
if __name__ == '__main__':
    list = [7,1,5,3,6,4]
    s = Solution()
    print(s.maxProfit(list))