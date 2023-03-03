#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        注意是每个字符串中都出现的共用字符,如果每个单词都出现了2次a,那就返回两个“a”,
        如果一个单词出现了一个a,其他的都出现了两次a,那最后只返回一个"a"
        也就是说每个单词都是一个记录26个字母出现次数的数组,一共有n个记录次数的数组
        我们每次取每个字母(每一列)对应的最小频率次数,然后拿着最后的次数数组,返回对应的字母结果
        """
        if not words:
            return []
        result = []
        # 先用第一个单词制作一个频率数组,便于和后面每个单词的频率数组对应字母的次数做比较
        hash = [0] * 26
        for i in words[0]:
            hash[ord(i)-ord("a")] += 1
        # 统计其他字符中每个字母出现的频率,
        # 每个单词统计后都要和第一个单词的对应字母位置的次数取最小
        for i in range(1, len(words)):
            hashOtherStr = [0] * 26
            for j in words[i]:
                hashOtherStr[ord(j)-ord("a")] += 1
            # 更新hash,取每个字母出现频率的最小值
            for k in range(26):
                hash[k] = min(hash[k], hashOtherStr[k])
        # 至此,每个字母共现在所有单词中的最小频率已经记录下来了，我们要映射回字母
        # 用chr函数从ASCII值映射到字母
        for i in range(26):
            while hash[i]!=0:
                result.extend(chr(i+ord("a")))
                hash[i] -= 1
        return result





# @lc code=end

