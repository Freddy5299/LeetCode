class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树
class Solution:
    def maxDepth(self, root) -> int:
        self.depth = []
        if root is None:
            return 0
        def add_to_result(level, node):
            """递归函数
            :param level int 当前在二叉树的层次
            :param node TreeNode 当前节点
            """


            self.depth.append(level) #写入该层的根节点
            #下发就是左右节点的遍历
            if node.left:
                add_to_result(level + 1, node.left)
            if node.right:
                add_to_result(level + 1, node.right)

        add_to_result(0, root)
        return max(self.depth) +1
if __name__ == '__main__':
    root = Node('3',Node('9'),Node('20',Node('15'),Node('7')))

    s = Solution()
    a = s.maxDepth(root)
    print(a)