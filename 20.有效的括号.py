#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        """
        "([)]" False
        "{[]}" True
        想不出来怎么用栈做啊这,第一次用栈解决问题,多学多思考即可
        栈结构的特殊性,本身就非常适合做对称匹配类的题目
        这里不匹配的情况可以概括为三种
        1.左边括号多余; 已遍历完字符串，但栈不为空，说明有左括号没有右括号来匹配
        2.括号不多余,但类型不匹配; 遍历字符串匹配的过程中，发现栈里没有要匹配的字符
        3.右边括号多余; 遍历字符串匹配的过程中,栈已经为空了,没有匹配的字符了,
                       说明右括号没有对应的左括号了
        
        字符串遍历完之后，栈是空的，就说明全都匹配
        """
        """
        最前方可以利用字符串长度为奇数来剪枝,直接去掉单类括号多余的情况
        这题用栈太卧槽了,整体思路就是,碰到了三种左括号,就将相应的右括号push进栈,
        碰到右括号就要去和栈顶的去比较,如果相同就pop掉,如果不同,那就直接False(因为不匹配)
        如果匹配过程中,栈空了则False; 如果匹配完了,栈还不空,则False
        """
        stack = []
        for item in s:
            if item=='(':
                stack.append(')')
            elif item=='[':
                stack.append(']')
            elif item=='{':
                stack.append('}')
            # 前面针对出现左括号的已经做完具体措施了,那么下面就是出现右括号时的匹配了
            # 那么,如果此时栈空了或者栈顶的右括号和stack[item]不同,那就False
            elif not stack or stack[-1]!=item:
                return False
            # 匹配上了就pop掉
            else:
                stack.pop()
        # 匹配完了栈还不空,那就不对了
        return True if not stack else False
            
                
# @lc code=end

