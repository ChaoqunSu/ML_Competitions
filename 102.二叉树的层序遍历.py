#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        层序遍历是广度优先遍历,用队列,先进先出
        被卡住的一点是怎么记录那一层有几个元素,
        实际上你在每层循环之前,队列中只剩那层的元素,用len就能获取了
        """
        # 所有的
        results = []
        # 每次都要先判根节点空不空
        if not root:
            return []
        
        from collections import deque
        # 注意一下队列初始化的方式
        que = deque([root])

        while que:
            size = len(que)
            # 每层的
            result = []
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)
                # 弹出cur之后要把cur的左右孩子加入队列(如果非空的话)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(result)
        
        return results


# @lc code=end

