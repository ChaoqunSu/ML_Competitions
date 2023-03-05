#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 这个和之前的那个四数相加不一样,注意区分,最主要的区别就是要去重
        # 涉及去重,一般就不适合再用哈希了,因为太麻烦了
        """
        想到了应该在15.三数之和的那个双指针的基础上去做,
        但是tmd,还是想不出来这咋用双指针做啊,无语
        我的疑惑点主要在于,三数之和是一个for循环加两个指针
        四数之和是两个for循环加两个指针,多的那个循环加在哪里？
        真是,唉就直接加在最前面就行了,
        第一个是k(第一个循环),第二个设为i(第二个循环),
        最外层就是k固定不动,然后就是三数之和的步骤,k后移,i也跟着后移
        """
        result = []
        # 一定不要忘了先排序
        nums.sort()
        for k in range(len(nums)):
            # 剪枝应该是有用的
            if nums[k]>target and nums[k]>0 and target >0:
                break
            # 去重
            if k>0 and nums[k]==nums[k-1]:
                continue
            for i in range(k+1,len(nums)):
                if nums[k] + nums[i]>target and nums[k]+nums[i]>0 and target >0:
                    break
                # 去重
                if (i > k+1) and nums[i]==nums[i-1]:
                    continue
                # 定义双指针,和三数之和是一样的
                left, right = i+1, len(nums)-1
                while(left<right):
                    total = nums[k]+nums[i]+nums[left]+nums[right]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        result.append([nums[k],nums[i],nums[left],nums[right]])
                        # 还有最后两个的去重,这一块很容易错,要多想想,
                        # 有可能left后面或者right前面重复很多步,所以我们要用while把重复的跨过去
                        # 用while要时卡住“left!=right",这里不等就是小于,因一个在变大，一个在变小
                        while left!=right and nums[left]==nums[left+1]: left += 1
                        while left!=right and nums[right-1]==nums[right]: right -= 1
                        # 去重之后不要忘了还有正常的指针移动
                        left += 1
                        right -= 1
        return result




# @lc code=end

