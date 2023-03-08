#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        后序遍历是:左右中
        """
        # 最下面是递归的方法,现在写一下迭代的方法,因为递归的实现本质就是栈,
        # 所以我们想用迭代法实现遍历,也需要用栈
        # 迭代法
        """
            迭代法用栈,因为后序遍历最后存结果的数组里面是'左右中'顺序。这里和前序遍历还不一样了，
        因为前序遍历('中左右')是要访问的元素和要处理的元素顺序是一致的，都是中间节点; 而后序遍历
        是得先探索到左边最下层的子节点，才能处理元素,所以这里需要变通一下,'左右中'不好搞,但是'中右左'
        好搞啊,就是前序遍历稍微调整一下即可,然后再在最后的result数组反转一下即可
        """  
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            # 仿照前序遍历(中左右),我们调整为中右左
            # 先把中节点处理
            node = stack.pop()
            result.append(node.val)
            # 先左子节点入栈,务必先判断左子节点空不空
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        # 此时结果数组是中右左,我们需要的是左右中,所以需要反转一下
        # 代码随想录反转竟然是直接return result[::-1],艹
        left, right = 0, len(result)-1
        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
        
        return result

        # 递归法
        # def postorder(root:TreeNode):
        #     if root == None:
        #         return
        #     postorder(root.left)
        #     postorder(root.right)
        #     result.append(root.val)

        # result = []
        # postorder(root)
        # return result

# @lc code=end

