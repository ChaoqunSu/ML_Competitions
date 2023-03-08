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
        # 迭代法
        """
            迭代法用栈,因为中序遍历存结果的数组里面是'左中右'顺序
            左孩子为空弹出自己,右孩子为空继续弹出
        """  
        
        # 代码随想录方法
        if not root:
            return []
        stack = []  # 不能提前将root结点加入stack中
        result = []
        cur = root
        # 只有指针为空且栈也空,才结束循环
        while cur or stack:
            # 先迭代访问最底层的左子树结点
            if cur:     
                stack.append(cur)
                cur = cur.left		
            # 到达最左结点后处理栈顶结点    
            else:		
                cur = stack.pop()
                result.append(cur.val)
                # 取栈顶元素右结点
                cur = cur.right	
        return result

        """
        # 下面是我自己的写法,但是超时了,而且不够简洁
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            # 左孩子为空弹出自己,右孩子为空继续弹出
            node = stack.pop()
            # 先访问到左边最底层
            while node:
                stack.append(node)
                node = node.left
            # 此while结束,说明到了左边最底层(碰到了null),此时将node(此即左边最底层的)的value再添加到result
            node = stack.pop()
            result.append(node.val)
            # 判此node有没有右孩子,没有就再从栈中弹出一个节点并添加到result
            if stack and not node.right:
                node = stack.pop()
                result.append(node.val)
            elif node.right:
                # 有右孩子就加入栈
                stack.append(node.right)        
        return result
        """
        



        # 递归法
        # def inorder(root:TreeNode):
        #     if not root:
        #         return
        #     inorder(root.left)
        #     result.append(root.val)
        #     inorder(root.right)

        # result = []
        # inorder(root)
        # return result
# @lc code=end

