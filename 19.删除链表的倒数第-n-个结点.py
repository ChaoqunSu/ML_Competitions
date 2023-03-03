#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 最下面是我自己的，想法是一样的，但是代码随想录用了虚拟头节点，更简洁一些
        # 重要的是用虚拟头节点可以规避一些极端情况的报错，因为返回的不是head而是dummy.next
        dummy_head = ListNode()
        dummy_head.next = head

        slow, fast = dummy_head, dummy_head
        # fast先往前走n步
        while(n!=0):
            fast = fast.next
            n -= 1
        while(fast.next!=None):
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return dummy_head.next
        """
        pre_n = head 
        cur = head 
        while(n):
            cur = cur.next
            n -= 1
        if not cur:
            head = head.next
            return head
        while(cur.next):
            pre_n = pre_n.next
            cur = cur.next
        if pre_n.next:
            pre_n.next = pre_n.next.next

        return head
        """
    
# @lc code=end

