class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        res = s[0]

        def extend(i, j, s):
            while (i >= 0 and j < len(s) and s[i] == s[j]):
                i -= 1
                j += 1
            return s[i + 1:j]

        for i in range(n - 1):
            e1 = extend(i, i, s)
            e2 = extend(i, i + 1, s)
            if max(len(e1), len(e2)) > len(res):
                res = e1 if len(e1) > len(e2) else e2
        return res

    def longestPalindromeMy(self, s: str) -> str:
        if len(s) <= 1: return s
        res = s[0]

        def extend(i, j, s):
            while (i >= 0 and j < len(s) and s[i] == s[j]):
                i -= 1
                j += 1
            return s[i + 1: j]

        for i in range(len(s) - 1):
            e1 = extend(i, i, s)
            e2 = extend(i, i + 1, s)
            if max(len(e1), len(e2)) > len(res):
                res = e1 if len(e1) > len(e2) else e2

        return res
if __name__ == '__main__':
    list = "babad"
    s = Solution()
    print(s.longestPalindromeMy(list))
