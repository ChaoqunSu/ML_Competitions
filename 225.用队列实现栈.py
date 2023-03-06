#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
from collections import deque
class MyStack:

    def __init__(self):
        # deque对象类似于双端队列
        self.queue = deque()
        
    def push(self, x: int) -> None:
        """
        把元素x压入栈顶
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        移除并返回栈顶元素
        """
        if self.empty():
            return None
        # 对于队列来说,需要先把尾部元素之前的元素移出并重新添加,
        # 才能使得对应于栈顶元素的元素漏出来
        # python的deque有popleft
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()


    def top(self) -> int:
        """
        返回栈顶元素
        """
        if self.empty():
            return None
        return self.queue[-1]


    def empty(self) -> bool:
        return not self.queue



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

