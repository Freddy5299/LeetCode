class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0: return 0
        return n // 5 + self.trailingZeroes(n // 5)
class Solutioncycle:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n = n // 5
            count += n
        return count
if __name__ == '__main__':
    s = Solution()
    n = 5
    print(s.trailingZeroes(n))