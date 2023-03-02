#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
"""

class Node(object):
    def __init__(self, x=0):
        self.val = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        # 定义虚拟头节点
        self.head = Node()
        # 设置个链表长度属性，便于后续操作，注意每次增和删都要更新
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        
        # 这里想确定范围只需找准极端临界值,比如找index=0即找头节点的值,
        # 那么当index=0下面的代码若是对的就行了;
        # 当index=0,cur就是虚拟头节点指向原头节点的指针,while跳过,返回的就是原头节点的val
        
        # 先定义一个临时指针，临时指针指向虚拟头节点指向的头节点
        cur = self.head.next
        # 当index非0时，也就是大于0时，执行，临时指针一个个往后遍历直到index对应的节点
        while(index):
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        
        # 想要在头部插入结点使得插入的节点成为新的头节点
        # 因为我们一直在用虚拟头结点,所以我们直接让新节点的指针指向原头节点,
        # 再让虚拟头节点的指针指向新头节点即可
        
        add_node = Node(val)
        # 新插入节点的指针指向了原头节点
        add_node.next = self.head.next
        # 虚拟头节点的指针指向新插入节点
        self.head.next = add_node
        # 记得更新链表长度size
        self.size += 1

    def addAtTail(self, val: int) -> None:
        # while循环到next指针为空时,即为尾节点
        add_node = Node(val)
        # 定义临时指针指向虚拟头节点
        cur = self.head
        while(cur.next):
            cur = cur.next
        # 循环结束后,cur临时指针指向尾节点
        cur.next = add_node
        # 记得更新链表长度
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index < 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        elif index > self.size:
            return
        add_node = Node(val)
        pre = self.head
        while(index):
            pre = pre.next
            index -= 1
        add_node.next = pre.next
        pre.next = add_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 and index >= self.size:
            return
        pre = self.head
        while(index):
            pre = pre.next
            index -= 1
        pre.next = pre.next.next
        self.size -= 1
"""


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)


    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        return cur.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(0, index)
        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

