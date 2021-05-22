# 根据一棵树的前序遍历与中序遍历构造二叉树。
#
# 注意:
# 你可以假设树中没有重复的元素。
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
from typing import List
from drawBinaryTree import draw_tree
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.val = value
        self.left = left  # 左子树
        self.right = right  # 右子树

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Node:
        if not preorder or not  inorder:
            return
        root = Node(preorder[0])
        idx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:1+idx],inorder[:idx])
        root.right =self.buildTree(preorder[1 + idx:], inorder[idx+1:])
        return root
def printPostorder(node):
    if node is None:
        return
    print(node.val)
    printPostorder(node.left)
    printPostorder(node.right)

if __name__ == '__main__':
    preorder = [1,2,4,5,3,6,7]
    inorder = [4,2,5,1,6,3,7,]
    s = Solution()
    a = s.buildTree(preorder,inorder)
    draw_tree(a)