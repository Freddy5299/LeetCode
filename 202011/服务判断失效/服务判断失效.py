from typing import List
class Solution:
    def removeDuplicates(self, str1: List[str], str2: List[str]) -> List:

        # str1 = 'a1-a2'.split('-')
        # str2 = 'a2-a3'.split('-')
        # map[str1[0]] = [str1[1]]
        # list1 = ['a5', 'a4']
        # map[str1[0]] += list1
        # print(map.__contains__('a1'))
        # if 'a1' is map.keys():
        #     print(map['a1'])
        # print(map)
        map = {}
        answer = []
        strt = str1[0].split(',')
        for i in strt:
            temple = i.split('-')
            map[temple[1]] = [temple[0]]
            if map.__contains__(temple[0]) is True:
                map[temple[1]] +=map[temple[0]]
        strt2 = str2[0].split(',')
        for i in strt2:
            if i not in answer:
                answer.append(i)
            for x in map[i]:
                if x not in answer:
                    answer += map[i]
        return answer
if __name__ == '__main__':
    list1 = ['a1-a2,a2-a3,a2-a4'] #排序数列
    list2 = ['a3,a4']  # 排序数列
    s = Solution()
    print(s.removeDuplicates(list1, list2))