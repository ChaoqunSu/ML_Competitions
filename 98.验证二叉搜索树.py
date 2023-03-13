#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        核心思想:是二叉搜索树等价于以中序遍历(左中右)节点时值单调递增
        但是有个大坑就是,每次不能只判断一个节点的左是否比它小/右是否比它大
        因为二叉搜索树是整个左子树的节点值都得比根节点的值小....
        """
        # 递归法
        # 提前定义pre全局指针
        pre = None
        def __isValidBST(root: TreeNode) -> bool: 
            nonlocal pre

            # 判空,空的啥都是
            if not root:
                return True
            # 开始递归,因为以中序遍历,所有节点的值必须单增才满足,
            # 这个过程其实和判断一个数组是不是单增有序是一样的,
            # 难点是不只是前后邻近的两个是前小后大,而是前面所有的都得比我小
            # 代码随想录建议用双指针,多思考多看看,
            # 其中一个指针就是记录前面的值用于和现在的值进行比较

            # 左
            is_left_valid = __isValidBST(root.left)

            # 中,注意第一轮先不给pre指针赋予节点,过了第一轮,前面腾出来一个节点再赋
            if pre and pre.val >= root.val: return False
            pre = root

            # 右
            is_right_valid = __isValidBST(root.right)

            return is_left_valid and is_right_valid
        
        return __isValidBST(root)
    """
    # 备选没那么优的方法:利用BST中序遍历特性,把树"压缩"成数组,判断数组是否有序即可
    def isValidBST(self, root: TreeNode) -> bool:
        # 思路: 利用BST中序遍历的特性.
        # 中序遍历输出的二叉搜索树节点的数值是有序序列
        candidate_list = []
        
        def __traverse(root: TreeNode) -> None: 
            nonlocal candidate_list
            if not root: 
                return 
            __traverse(root.left)
            candidate_list.append(root.val)
            __traverse(root.right)
            
        def __is_sorted(nums: list) -> bool: 
            for i in range(1, len(nums)): 
                if nums[i] <= nums[i - 1]: # ⚠️ 注意: Leetcode定义二叉搜索树中不能有重复元素
                    return False
            return True
        
        __traverse(root)
        res = __is_sorted(candidate_list)
        
        return res
    """

        
# @lc code=end

