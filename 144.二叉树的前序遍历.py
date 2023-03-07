#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        巧的记忆方法：这里前中后，其实指的就是中间节点的遍历顺序
        1.前序遍历：中左右
        2.中序遍历：左中右
        3.后序遍历：左右中
        所以我们这里前序遍历是中左右的顺序
        root存的方式好像就是中左右,只不过里面有null
        """
        result = []
        
        def traversal(root: TreeNode):
            if root == None:
                return
            result.append(root.val) # 前序
            # 递归是重复调用函数自身实现循环
            traversal(root.left)    # 左
            traversal(root.right)   # 右

        traversal(root)
        return result
        
# @lc code=end

