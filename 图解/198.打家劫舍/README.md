##198.打家劫舍
### 1.题目
![tn8C59.jpg](https://s1.ax1x.com/2020/05/29/tn8C59.jpg)
### 2.思路
[![tn8pE4.md.jpg](https://s1.ax1x.com/2020/05/29/tn8pE4.md.jpg)](https://imgchr.com/i/tn8pE4)
### 3.代码
```python
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
```
### 4.真心话
动态规划的难点就是寻找子问题的求解过程，需要把大问题拆分成简单的小问题，思路和想法都是一步步积累，慢慢成长的。
只有当具备这种思维能力之后这种问题才会信手拈来，不然就乖乖多思考多总结吧。