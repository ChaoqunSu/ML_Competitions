#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 直接暴力求解的话，就是两个for循环嵌套着，把所有可能都匹配一次
        # 暴力超时，考虑优化的想法，滑动窗口(即只用一个for循环)
        slow = 0
        res = float("inf")
        n = len(nums)
        Sum = 0
        if sum(nums) < target:
            return 0
        for i in range(n):
            Sum += nums[i]
            while Sum >= target:
                res = min(res, i - slow+1)
                Sum -= nums[slow]
                slow += 1
                
        return res

            
# @lc code=end

