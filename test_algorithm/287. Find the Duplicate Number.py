#给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

#想法，首先就是遍历，然后对应有一个空余指针的问题，但是不太适用。也可以使用排序nlogn，然后使用指针平移比较元素就好了。

# 【笔记】这道题（据说）花费了计算机科学界的传奇人物Don Knuth 24小时才解出来。并且我只见过一个人（注：Keith Amling）用更短时间解出此题。
#
# 快慢指针，一个时间复杂度为O(N)的算法。
#
# 其一，对于链表问题，使用快慢指针可以判断是否有环。
#
# 其二，本题可以使用数组配合下标，抽象成链表问题。但是难点是要定位环的入口位置。
#
# 举个例子：nums = [2,5, 9 ,6,9,3,8, 9 ,7,1]，构造成链表就是：2->[9]->1->5->3->6->8->7->[9]，也就是在[9]处循环。
#
# 其三，快慢指针问题，会在环内的[9]->1->5->3->6->8->7->[9]任何一个节点追上，不一定是在[9]处相碰，事实上会在7处碰上。
#
# 其四，必须另起一个for循环定位环入口位置[9]。这里需要数学证明。
#
# 对“其四”简单说明一下，既然快慢指针在环内的某处已经相碰了。那么，第二个for循环遍历时，res指针还是在不停的绕环走，但是必定和i指针在环入口处相碰。
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums : return
        temp = [0]*(len(nums) +1)
        for index,i in enumerate(nums):

            if not i in temp:
                temp[i] = i
            else:
                return i

class SolutionMY:
    def findDuplicate(self, nums: List[int]) -> int:
        # 二分法
        if not nums : return
        left= 1
        right = len(nums)-1
        while(left < right):
            count = 0
            mid = (left+right)//2
            for i in nums:
                if i <=mid:
                    count +=1
            if count<=mid:
                left =mid +1
            else:
                right = mid
        return left

class Solutionsm:
    def findDuplicate(self, nums: List[int]) -> int:
        # 快慢指针 经典例题
        slow = 0
        fast = 0
        while (1):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if (slow == fast):
                break
        find = 0
        while (1):
            find = nums[find]
            slow = nums[slow]
            if (find == slow):
                return find
if __name__ == '__main__':
    s = SolutionMY()
    nums = [1,2,4,3,1,5]
    print(s.findDuplicate(nums))