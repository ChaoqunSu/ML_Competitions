#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 只需指针反向
        # 初始化很重要
        cur = head
        pre = None
        while(cur):
            # 必须有个temp来存cur.next，因为你要改方向，改完就不知道原来的方向了，所以先存下来
            temp = cur.next
            # 改为指向pre
            cur.next = pre
            # 更新pre和cur，即后移，一定要先更新pre，因为要让pre更新为现在的cur，一旦先更新cur了，pre就没法更新了
            pre = cur
            cur = temp
        # 返回新的头节点，cur结束完循环，指向了原链表的空(pre此时指向最后一个节点)
        return pre




# @lc code=end

