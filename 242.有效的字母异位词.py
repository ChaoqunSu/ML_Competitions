#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        一开始被吓住了,没有想到字母只有26个这种隐条件,那么其实可以用一个26长的数组来存各个字母出现的次数即可
        这里要用到内置函数ord,将字母映射为对应的ASCII值
        """
        record = [0] * 26
        # 只需记录下来所有字母的ASCII值和"a"的ASCII值的相对值即可
        # s里面有的字母，对应位置+1,t也有的，对应位置-1，最后只要这个数组全是0元素，那这俩就是字母异位词
        for i in s:
            record[ord(i)-ord("a")] += 1
        for j in t:
            record[ord(j)-ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
        return True
        
# @lc code=end

