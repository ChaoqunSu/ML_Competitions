#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 因为要去重，且是返回满足条件的元素而非下标
        # 单单因为去重，就已经不适合用哈希法了
        # 改用双指针法，这里的双指针法用的很妙
        """
        这里最重要的一点就是先把数组按从小到大排个序
        for循环用来遍历,下标为i,left指针放在i+1位置,right指针放在最末端位置
        如果这三个数相加大于0,那right就往左移,如果小于0,left就往右移
        """
        # 定义结果列表
        result = []
        # 先排序
        nums.sort()
        for i in range(len(nums)):
            # 排序之后如果第一个元素已经大于零，那么无论如何组合都不可能凑成三元组，直接返回结果就可以了
            if nums[i] > 0: 
                break
            # 要对nums[i]去重,比如现在的nums[i]和前面的nums[i-1]相等,那就跳过去
            if i>=1 and nums[i-1]==nums[i]:
                continue
            # 开始指针运算的循环,因为left和right指针往中间合,
            # 所以循环条件应该是left<right,不能等，因为left和right指向的必须是不同的元素
            left, right = i+1, len(nums)-1
            while left<right:
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    # 去重逻辑很重要，总是想不清楚
                    # 要考虑对后两位去重,因为考虑到如果是-3,1,1,1,2,2,2,最终的结果应该是[[-3,1,2]]
                    # 而不是[[-3,1,2],[-3,1,2],[-3,1,2]]
                    while left != right and nums[left] == nums[left + 1]: left += 1
                    while left != right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
        return result
# @lc code=end

