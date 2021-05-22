class Solution:
    def reverseBit(self, n):
        result = 0
        for i in range(32):
            result = (result << 1) + (n & 1)
            n >>= 1
        return result

# if __name__ == '__main__':
#     s = Solution()
#     n = 0b10000000000000000000000000000000
#     print(s.reverseBit(n))
#     print(bin(n))
#     print(bin(s.reverseBit(n)))