#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 不管重合不重合，重合的部分都在后面，
        # 那么前面可以先让二者赶齐，即让长的提前先走几步赶到和短的一样长，然后再一起循环匹配
        # 那我们先得到两个链表的长度
        lenA, lenB = 0, 0
        len_headA, len_headB = headA, headB
        while(len_headA):
            len_headA = len_headA.next
            lenA += 1
        while(len_headB):
            len_headB = len_headB.next
            lenB += 1
        curA, curB = headA, headB
        # 让其中一个一定是最长的，我们后面只让这个长的先走几步
        if lenA > lenB:
            # 让B一定是最长的,并着写竟然就能同时互换值，懵逼，但是确实是并行交换的
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA
        for _ in range(lenB-lenA):
            curB = curB.next
        # 此时，就后续直至交叉处的长度来说，curA和curB是同一起点了
        while(curA):
            if curA == curB:
                return curA
            
            curA = curA.next
            curB = curB.next
        return None

        
# @lc code=end

