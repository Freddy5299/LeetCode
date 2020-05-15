# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# Output: [1,2,2,3,5,6]
from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merge = []
        n1 =0
        if (m or n) == 0:
            return None
        for i in range(max(len(nums1),len(nums2))):
            if nums1[i] ==nums2[n1]:
                merge.append(nums1[i])
                merge.append(nums2[n1])
                n1 =+1
            elif nums1[i] > nums2[n1]:
                n1 +=1
                merge.append(nums2[n1])
            elif nums1[i] < nums2[n1]:
                merge.append(nums1[i])
        return merge
    def merge1 (self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m - 1] <= nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
        """
        由于没有使用 current，第一步比较结束后有两种情况:
            1. 指针 m>0，n=0，此时不需要做任何处理
            2. 指针 n>0，m=0，此时需要将 nums2 指针左侧元素全部拷贝到 nums1 的前 n 位
        """
        if n > 0:
            nums1[:n] = nums2[:n]
        return nums1
    def merge2 (self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        nums1[:] = sorted(nums1[:m] + nums2)
        return nums1
if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    s = Solution()
    print(s.merge1(nums1, m ,nums2,n))