#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        # 实际上不是个数学题，而是注意到“无限循环”，不是快乐数的会陷入无限循环,
        # 也就是有个结果反复出现，陷入死循环,那这个数就不是快乐数
        def calculate_happy(num):
            sum_ = 0
            
            # 从个位开始依次取，平方求和
            # 这个取每位数计算的过程要知道
            while num:
                sum_ += (num % 10) ** 2
                num = num // 10
            return sum_

        # 记录中间结果
        record = set()

        while True:
            n = calculate_happy(n)
            if n == 1:
                return True
            
            # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
            if n in record:
                return False
            else:
                record.add(n)
# @lc code=end

