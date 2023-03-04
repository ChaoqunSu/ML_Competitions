#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 这是自己做的暴力解法,代码随想录给的哈希法更好一些
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # 之所以会用哈希法,是因为我们只需要找两个数之和,给定一个数之后,另一个数就是target-该数,
        # 直接去找该数在不在哈希表里面即可
        match_dict = {}
        for i in range(len(nums)):
            match = target - nums[i]
            if match in match_dict.keys():
                return [match_dict[match],i]
            else:
                match_dict[nums[i]] = i
        return []

# @lc code=end

