# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。

# 使用一个计数器,遍历每个元素,当遇到其他元素使计数器-1，相同+1,为0更换新的元素
from typing import List
class Solution:
    def majorityElement(self,nums:List[int]) ->int :
        count, majority = 1, nums[0]
        for num in nums[1:]:
            if count == 0:
                majority = num
            if num == majority:
                count+=1
            else:
                count -= 1
        return majority
