#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 反转字符串中的单词
#

# @lc code=start
class Solution:
    def trim_spaces(self, s):     
        n = len(s)
        left = 0
        right = n-1
    
        while left <= right and s[left] == ' ':    #去除开头的空格
            left += 1
        while left <= right and s[right] == ' ':   #去除结尾的空格
            right -= 1
        tmp = []
        while left <= right:                      #去除单词中间多余的空格
            if s[left] != ' ':
                tmp.append(s[left])
            elif tmp[-1] != ' ':                 #当前位置是空格，但是相邻的上一个位置不是空格，则该空格是合理的
                tmp.append(s[left])
            left += 1
        return tmp
    # 反转字符数组
    def reverse_string(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return None
    # 反转每个单词
    def reverse_each_word(self, nums):
        start = 0
        end = 0
        n = len(nums)
        while start < n:
            while end < n and nums[end] != ' ':
                end += 1
            self.reverse_string(nums, start, end-1)
            start = end + 1
            end += 1
        return None

    def reverseWords(self, s: str) -> str:
        """
        注意一个str里面是按字母、空格为基本元素的,而不是单词
        例子:"the sky is blue "
        移除多余空格:"the sky is blue"
        字符串反转:"eulb si yks eht"
        单词反转:"blue is sky the"        
        """
        # 移除多余空格
        # python 提供删除字符串的方法
        # strip():删除字符串前后(左右两侧)的空格或特殊字符
        # s = s.strip()
        # 代码随想录是自己写的去空格函数
    
        # 反转
        #测试用例："the sky is blue"  
        # ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']             
        l = self.trim_spaces(s)    
        #['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']           
        self.reverse_string(l,  0, len(l)-1)  
        #['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']
        self.reverse_each_word(l)             
        return ''.join(l) 
        
         
# @lc code=end

