#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 这道题差点把我搞死，下面会把坑总结出来
        # 一定要加虚拟节点，这样才能保持每一轮的规律一样，不然根本搞不出来可循环的规律
        res = ListNode(next=head)
        # 别直接拿着res去玩，赋出去，也方便最后确定新的头节点
        pre = res

        # 搞完虚拟头节点就是循环规律了，每轮都是三个节点参与变化
        # 但是千万不要单独弄三个指针去指向三个节点，不然大罗神仙也救不了了，全乱套了就
        # 在循环里，后面俩节点全部依赖于pre，每轮更新pre时，后面俩也会随之更新，
        # 每个新的循环都一直更在pre的后面

        # 只有后面两个节点都不空时，才能循环
        while(pre.next and pre.next.next):
            cur = pre.next
            post = pre.next.next

            # 开始变化
            pre.next = post
            temp = post.next
            post.next = cur
            cur.next = temp

            # 更新pre,不管pre后头那俩乱成啥我不管，我只管把pre后移两位
            pre = pre.next.next
        # 返回新头节点，也就是虚拟头节点的next，这个是最可靠的
        return res.next
# @lc code=end

