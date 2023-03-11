#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        唉,又是一道递归法贼简单,但是没想出来的题,核心思想就是判断 
        左子树的左和右子树的右, 左子树的右和右子树的左
        是否一样
        """
        if not root:
            return True
        return self.compare(root.left, root.right)
    
    def compare(self,left,right):
        #首先排除空节点的情况
        if left == None and right != None: return False
        elif left != None and right == None: return False
        elif left == None and right == None: return True

        # 数值不相同,则不匹配
        elif left.val != right.val: return False

        # 此时就是：左右节点都不为空，且数值相同的情况
        # 此时才做递归，做下一层的判断
        # 左子树的左和右子树的右
        outside = self.compare(left.left, right.right)
        # 左子树的右和右子树的左
        inside = self.compare(left.right, right.left)
        # 前面这两行会反复调用该函数,
        # 直到执行完了这两行,
        # outside和inside都会得到前面四句if和elif返回的True/False
        # 逻辑处理
        isSame = outside and inside
        return isSame
        



# @lc code=end

