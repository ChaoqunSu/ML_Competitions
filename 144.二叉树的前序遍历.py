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
        # 最下面是递归的方法,现在写一下迭代的方法,因为递归的实现本质就是栈,
        # 所以我们想用迭代法实现遍历,也需要用栈

        # 迭代法
        """
            迭代法用栈,因为最后存结果的数组里面是'中左右'顺序, 那么push进栈的
        顺序应该是先push父节点,父节点弹出,再push进去右子节点,然后再push进左子节点
        """  
        # 根节点为空,则返回空列表
        if not root:
            return []
        # 定义栈,注意！！！栈中存放的是树节点这种结构体,结构体有value和指向左右子节点的指针
        stack = [root]
        result = []
        # 栈不空时执行循环
        while stack:
            # 先把根节点pop出来
            node = stack.pop()
            # pop出来后先把该节点的calue存入结果数组(这就是‘中左右’的中)
            result.append(node.val)
            # 右孩子先入栈
            if node.right:
                stack.append(node.right)
            # 左孩子后入栈
            if node.left:
                stack.append(node.left)
        
        return result             

        # 递归法
        # def traversal(root: TreeNode):
        #     if root == None:
        #         return
        #     result.append(root.val) # 前序
        #     # 递归是重复调用函数自身实现循环
        #     traversal(root.left)    # 左
        #     traversal(root.right)   # 右

        # result = []
        # traversal(root)
        # return result
        
# @lc code=end

