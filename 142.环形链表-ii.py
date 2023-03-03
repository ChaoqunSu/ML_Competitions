#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        这道题有点难啊艹,想不到用快慢指针就gg了,凉透.
        首先我们怎么判断有没有环,我们会定义一个快指针(一次走两个节点)和慢指针(一次走一个节点),
        只要fast和slow指针相遇了就说明链表有环,然后就是接下来怎么搞.设头节点到环入口为x,
        fast先进环,走了n圈之后,才在环里遇到slow,遇到的位置距离环入口为y,此处再走z就又到环
        (即一圈就是y+z), 遇到时有,(x+y)*2 = x+y+n(y+z),得x=(n-1)*(y+z)+z,n=1时有x=z
        """
        # 定义快慢指针
        slow, fast = head, head
        # 环至少得有两个节点,如果但凡fast.next是null,那就没有环
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 如果相遇了,那就有x=(n-1)*(y+z)+z,n=1时有x=z
            if slow==fast:
                # 此时定义两个指针,一个从head开始跑,另一个从快慢指针相遇处开始跑,二者相遇之处就是环入口
                # 不用管后者跑了几圈
                p = head
                q = slow
                while p!=q:
                    p = p.next
                    q = q.next
                # return p或q皆可
                return p
        return None

# @lc code=end

