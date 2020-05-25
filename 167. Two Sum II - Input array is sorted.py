# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

# 技法 大就缩小就涨
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}
        for index, number in enumerate(numbers):
            if (target - number) in visited:
                return [visited[target - number], index + 1]
            else:
                visited[number] = index + 1

    def twoSumgood(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[right] + numbers[left] < target:
                left += 1
            if numbers[right] + numbers[left] > target:
                right -= 1
            if numbers[right] + numbers[left] == target:
                return [left, right]


if __name__ == '__main__':
    list = [2, 7, 11, 15]
    s = Solution()
    print(s.twoSumgood(list, 9))
