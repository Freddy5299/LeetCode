from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max__dp = [1] * (n + 1)
        min_dp = [1] * (n + 1)
        ans = float('-inf')
        print(max__dp)
        print(min_dp)
        for i in range(1, n + 1):
            max__dp[i] = max(max__dp[i - 1] * nums[i - 1],
                             min_dp[i - 1] * nums[i - 1], nums[i - 1])
            min_dp[i] = min(max__dp[i - 1] * nums[i - 1],
                            min_dp[i - 1] * nums[i - 1], nums[i - 1])
            ans = max(ans, max__dp[i])
        return ans

    def maxProduct1(self, nums: List[int]) -> int:
        n = len(nums)
        a = b = 1
        ans = float('-inf')

        for i in range(1, n + 1):
            temp = a
            a = max(a * nums[i - 1],
                    b * nums[i - 1], nums[i - 1])
            b = min(temp * nums[i - 1],
                    b * nums[i - 1], nums[i - 1])
            ans = max(ans, a)
        return ans
    def maxProductMy(self,nums:List[int]) ->int:
        ans = float('-inf')
        n = len(nums)
        max_dp = [1]*(n + 1)
        min_dp = [1]*(n + 1)
        for i in range(1,n+1):
            max_dp [i] = max(max_dp[i-1]*nums[i-1],min_dp[i-1]*nums[i-1],nums[i-1])
            min_dp[i] = max(max_dp[i - 1] * nums[i - 1], min_dp[i - 1] * nums[i - 1], nums[i - 1])
            ans = max(max_dp [i],ans)
        return ans
if __name__ == '__main__':
    list = []
    s = Solution()
    print(s.maxProductMy(list))