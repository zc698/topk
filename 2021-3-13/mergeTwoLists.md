21.合并两个有序链表
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接两个链表的所有节点组成的。

输入：l1 = [1,2,4], l2 = [1,3,4]

输出：[1,1,2,3,4,4]

思路：list1[0] + merge(list1[1:],list2) list1[0] < list2[0];list2[0] + merge(list1,list2[1:]) otherwise
两个链表头部值较小的一个节点与剩下元素的merge操作结果合并

来源：力扣（LeetCode）

链接：https://leetcode-cn.com/problems/merge-two-sorted-lists

    class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

时间复杂度：O(n + m)， n和m表示两个链表的长度

空间复杂度：O(n + m) ，n和m表示两个链表的长度