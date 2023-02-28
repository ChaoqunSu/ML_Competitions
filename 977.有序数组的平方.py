#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        n = len(nums)
        new_ls = [0] * n
        for i in range(len(nums)):
            lf = nums[left] * nums[left]
            rh = nums[right] * nums[right]
            if lf <= rh:
                new_ls[n-1-i] = rh
                right -= 1
            else:
                new_ls[n-1-i] = lf
                left += 1
        return new_ls

# @lc code=end

