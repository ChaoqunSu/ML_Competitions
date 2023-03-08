#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        中序遍历:左中右
        """
        def inorder(root:TreeNode):
            if not root:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)

        result = []
        inorder(root)
        return result
# @lc code=end

