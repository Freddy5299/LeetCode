from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if not nums:return 0
        dp = [0]*(N+1)
        dp[1] =nums[0]
        for i in range(2,N+1):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i-1])
        return dp[N]

if __name__ == '__main__':
    nums=[2,10,9,3,1,1]
    s = Solution()
    a = s.rob(nums)
    print(a)

