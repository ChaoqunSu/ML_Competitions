#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 递归法(前序遍历)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        前序遍历:中左右
        """
        if not root:
            return 
        root.left, root.right = root.right, root.left
        self.invertTree(root.right)
        self.invertTree(root.left)

        return root
    # 下面这种是最麻烦的层序遍历迭代法(我自己写的),其实上面的递归法更简单
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root:
    #         return 
    #     from collections import deque
    #     que = deque([root])

    #     while que:
    #         size = len(que)
    #         for _ in range(size):
    #             cur = que.popleft()
    #             cur.left, cur.right = cur.right, cur.left
    #             if cur.left:
    #                 que.append(cur.left)
    #             if cur.right:
    #                 que.append(cur.right)
        
    #     return root
                


# @lc code=end

