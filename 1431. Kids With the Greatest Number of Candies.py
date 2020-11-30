from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        ret = [candy + extraCandies >= maxCandies for candy in candies]
        return ret

if __name__ == '__main__':
    s = Solution()
    candies = [2,3,5,1,3]
    extraCandies = 3
    answer = s.kidsWithCandies(candies,extraCandies)
    print(answer)
