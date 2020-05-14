class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树



# class Solution:
#     def levelOrder(self, root) :
#         """递归法 用时中等"""
#         if root is None:
#             return []
#
#         result = []
#
#         def add_to_result(level, node):
#             """递归函数
#             :param level int 当前在二叉树的层次
#             :param node TreeNode 当前节点
#             """
#             if level > len(result) - 1: #先对比层级，如果是新的层，就在result里面加一个空层
#                 result.append([])
#
#             result[level].append(node.val) #写入该层的根节点
#             #下发就是左右节点的遍历
#             if node.left:
#                 add_to_result(level + 1, node.left)
#             if node.right:
#                 add_to_result(level + 1, node.right)
#
#         add_to_result(0, root)
#         return result


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #  用时较短结束条件：
        if not root: return []

        # BFS
        res = []
        queue = [root]
        while queue:
            row = []
            for _ in range(len(queue)):
                print(_)
                node = queue.pop(0)
                row.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(row)
        return res

if __name__ == '__main__':


    root = Node('3',Node('9'),Node('20',Node('15'),Node('7')))

    s = Solution()
    a = s.levelOrder(root)
    print(a)