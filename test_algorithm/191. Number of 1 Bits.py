class Solution:
    def hammingWeight(self, n):
        count = 0
        print('debug n=',n)
        while n:
            print('debug ####n=', bin)
            n &= n-1
            count +=1

        return count
if __name__ == '__main__':
    s = Solution()
    n= 0b00000000000000000000000000001011
    print(s.hammingWeight(n))