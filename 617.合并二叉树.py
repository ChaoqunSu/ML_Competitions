#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        重复使用了题目给出的节点而不是创建新节点. 节省时间, 空间
        前面学遍历是有原因的啊,你要进行各种操作总要先确定一种遍历方式不是吗
        这里你要先确定一种遍历方式,确定下来别摇摆,再去进行下一步操作,如用前序遍历(中左右)
        """
        if not root1:
            return root2
        if not root2:
            return root1
        # 进行到此处是,root1和root2都非空
        # 中
        root1.val += root2.val
        # 到这里又开始发迷了,你这里不要再去想什么如果root1.left是空的咋办,
        # 那是下一个递归里面前面的两个if会去处理,和此轮循环没关系啊
        # 左
        root1.left = self.mergeTrees(root1.left,root2.left)
        # 右
        root1.right = self.mergeTrees(root1.right,root2.right)

        return root1

# @lc code=end

