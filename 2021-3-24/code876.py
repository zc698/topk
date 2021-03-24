876.链表的中间结点
给定一个头结点为 head 的非空单链表，返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。
输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/middle-of-the-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
对链表进行遍历，同时将遍历到的元素依次放入数组 A 中。如果我们遍历到了 N 个元素，
那么链表以及数组的长度也为 N，对应的中间节点即为 A[N/2]。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]
        
        
时间复杂度：O(N)，N是给定链表的结点数目。
空间复杂度：O(N)，数组A用去的空间。


思路二：
运用快慢指针法，用两个指针 slow 与 fast 一起遍历链表。slow 一次走一步，fast 一次走两步。那么当 fast 到达链表的末尾时，slow 必然位于中间。
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        first = slow = head
        while first and first.next:
            slow = slow.next
            first = first.next.next
        return low

时间复杂度：O(N)，N是给定链表的结点数目。
空间复杂度：O(1)，只需要常数空间存放 slow 和 first 两个指针。



