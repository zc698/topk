code19
删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#思路：使用两个指针first 和 second 同时对链表进行遍历，并且first 比 second 超前n 个节点。当first 遍历到链表的末尾时，second 就恰好处于倒数第n 个节点。


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0,head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next

        return dummy.next

#时间复杂度：O(N),N为链表的长度。
#空间复杂度：O(1)
