#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    # 2
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[slow] = nums[i]
                slow += 1
        return slow
# @lc code=end
        
