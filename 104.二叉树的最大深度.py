#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 最下面是自己写的迭代法,利用层次遍历来找最大深度,一开始想用递归法,一直卡着没写出来
    # 递归法,看着简单,但是很难,一定要琢磨透
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.getDepth(root)
    
    def getDepth(self, root: Optional[TreeNode]):
        # 先判空不空
        if not root:
            return 0
        leftheight = self.getDepth(root.left)
        rightheight = self.getDepth(root.right)
        # 因为走到这一步的一定是非空的,1本身就是初始化也是每次的递增值
        height = 1 + max(leftheight, rightheight)
        return height


    # 迭代法,层序遍历
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     """
    #     其实就是有多少层,如果用队列,最远子节点那一层一定是最后出队列的
    #     """
    #     if not root:
    #         return 0
    #     from collections import deque
    #     que = deque([root])
    #     i = 0
    #     while que:
    #         size = len(que)
    #         for _ in range(size):
    #             cur = que.popleft()
    #             if cur.left:
    #                 que.append(cur.left)
    #             if cur.right:
    #                 que.append(cur.right)
    #         i += 1

    #     return i
            
# @lc code=end

