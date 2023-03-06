#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        in主要负责push,out主要负责pop
        """
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        """
        有新元素进来,就往in里面push
        """
        self.stack_in.append(x)

    def pop(self) -> int:
        """
        从队列开头移除并返回元素
        要把stack_in的元素移进stack_out
        """
        # 判队列空不空
        if self.empty():
            return None
        # 出栈不空的话,就直接让出栈pop出来那个元素(此元素就是对应队列中的头部元素)
        if self.stack_out:
            return self.stack_out.pop()
        # 出栈是空的话,就要把入栈的所有元素都移进出栈,
        # 此时出栈出来的第一个元素就是对应队列的头部元素
        else:
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        """
        返回队列开头的元素,即get头部元素
        可以利用pop()得到头部元素,但是pop()会把头部元素弹出去
        那我们再把它添加回来即可
        """
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self) -> bool:
        """
        只要in或者out有元素,说明队列不为空;都没有元素才是空的
        """
        return not (self.stack_in or self.stack_out)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

