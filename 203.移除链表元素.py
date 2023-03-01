#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 添加一个虚拟节点
        dummy_head = ListNode(next=head)
        cur = dummy_head
        # 判定，下一个节点不空
        while(cur.next!=None):
            # cur.next指的是下一个节点，val是下一个节点储存的值
            # 如果下一个节点的值(data)等于目标，就跳过它(也就相当于删掉它)
            if(cur.next.val == val):
                # 指向下一个节点变为指向下下一个节点
                cur.next = cur.next.next
            # 如果下一个节点的值不等于目标，就让cur这个临时指针往后去遍历 
            else:
                cur = cur.next
        # 返回虚拟节点的next(其实也就是原来的head)
        return dummy_head.next

# @lc code=end

