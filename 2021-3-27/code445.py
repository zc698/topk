445.两数相加
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

日期：2021.3.27

思路：
把所有数字压入两个栈中，再依次取出相加。计算过程中需要注意进位的情况。

时间复杂度：O(max(m,n))
空间复杂度：O(m + n)

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		s1 = []
		s2 = []
		while l1:
			s1.append(l1.val)
			l1 = l1.next
		while l2:
			s2.append(l2.val)
			l2 = l2.next
		flag = 0
		ans = None
		while s1 or s2 or flag > 0:
			a = 0 if not s1 else s1.pop()
			b = 0 if not s2 else s2.pop()
			c = a + b + flag
			flag = c // 10
			c = c % 10
			node = ListNode(c)
			node.next = ans
			ans = node
			
		return ans
			
			
			
			
		
		
		
		
		
