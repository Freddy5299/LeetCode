from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums:
            slow = 0
            for fast in range(1, len(nums)):
                if nums[fast] != nums[slow]:
                    slow += 1
                    nums[slow] = nums[fast]
            print(nums[:slow+1])
            return slow + 1
        else:
            print(nums)
            return 0


if __name__ == '__main__':
    list = [1,1,2,3,4,5,6,6,6,] #排序数列
    s = Solution()
    print(s.removeDuplicates(list))