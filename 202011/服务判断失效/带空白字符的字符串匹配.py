from typing import List
class Solution:
    def removeDuplicates(self, str1: List[str], str2: List[str]) -> int:
        len2 = len(str2[0])
        times = 0
        for i in range(len(str1[0])):
            for j in range(len2):
                if str1[0][i+j] is ' ':
                    if str1[0][i+j+1] !=str2[0][j]:
                        break
                else:
                    if str1[0][i+j] !=str2[0][j]:
                        break
                if j ==len2-1:
                    times +=1
        return times
if __name__ == '__main__':
    list1 = ['Abbbbbbbb bca acb bd'] #排序数列
    list2 = ['bbb']  # 排序数列
    s = Solution()
    print(s.removeDuplicates(list1, list2))