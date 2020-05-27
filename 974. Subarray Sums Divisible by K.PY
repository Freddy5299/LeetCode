#给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
#之前出过
from typing import List
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        record = {0: 1}
        total, ans = 0, 0
        for elem in A:
            total += elem
            modulus = total % K
            same = record.get(modulus, 0)
            ans += same
            record[modulus] = same + 1
        return ans

if __name__ == '__main__':
    s = Solution()
    A = [4, 5, 0, -2, -3, 1]
    K = 5
    ans = s.subarraysDivByK(A,K)
    print(ans)