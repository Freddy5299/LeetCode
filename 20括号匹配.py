class Solution1:
    def isValid(self, s):
        stack = []
        map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }
        for x in s:
            if x in map:
                stack.append(map[x])
                #这一步就很巧妙，把左括号对应的右括号压进去，这样在后面的比对的时候就可以使用等于
            else:
                if len(stack) != 0:
                    top_element = stack.pop()
                    if x != top_element:
                        return False
                    else:
                        continue
                else:
                    return False
        return len(stack) == 0


# class Solution:
#     def isValid(self,s):
#         if len(s) % 2 != 0:
#             return False
#         while '()' in s or '[]' in s or '{}' in s:
#             s = s.replace('[]', '').replace('()', '').replace('{}', '')
#         return True if s == '' else False

class Solution_my:
    def isValid(self, s):
        stack = []
        map = {
            '{':'}',
            '(':')',
            '[':'}'
        }
        for i in s:
            if i in map:
                stack.append(map[i])
            else:
                if stack !=0:
                    top = stack.pop()
                    if top == i:
                        continue
                    else:
                        return False
                else:
                    return False
        return stack == []
if __name__ == '__main__':
    data = '({})'
    s = Solution_my()
    result = s.isValid(data)
    print(result)