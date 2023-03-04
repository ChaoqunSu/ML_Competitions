#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 最下面隐去的是自己的暴力解法，没有用哈希表，时间复杂度太高了，我们主要看一下哈希表方法怎么做
        # 代码随想录这个给的还是很好的
        # 建立一个字典,key是数字,value用来做标志,nums1中有就是1,nums2也有该数就添加到结果中，然后把value置零
        # 这主要是利用了key不可重复，这很关键
        val_dict = {}
        result = []
        for num in nums1:
            # nums1里面二等所有数(去重)都作为key，并赋予value1
            val_dict[num] = 1
        
        for num in nums2:
            if num in val_dict.keys() and val_dict[num]==1:
                result.append(num)
                val_dict[num] = 0
        
        return result
        # len1 = len(nums1)
        # len2 = len(nums2)
        # result = []
        # for i in range(len1):
        #     if nums1[i] in result:
        #             continue
        #     for j in range(len2):
        #         if nums2[j] in result:
        #             continue
        #         if nums1[i] == nums2[j]:
        #             result.append(nums1[i])
        # return result
# @lc code=end

