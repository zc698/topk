445.�������
�������� �ǿ� ���������������Ǹ��������������λλ������ʼλ�á����ǵ�ÿ���ڵ�ֻ�洢һλ���֡�����������ӻ᷵��һ���µ�����

����Լ���������� 0 ֮�⣬���������ֶ��������㿪ͷ��

���룺(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
�����7 -> 8 -> 0 -> 7

���ף�

��������������޸ĸ���δ������仰˵���㲻�ܶ��б��еĽڵ���з�ת��

��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/add-two-numbers-ii
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������

���ڣ�2021.3.27

˼·��
����������ѹ������ջ�У�������ȡ����ӡ������������Ҫע���λ�������

ʱ�临�Ӷȣ�O(max(m,n))
�ռ临�Ӷȣ�O(m + n)

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
			
			
			
			
		
		
		
		
		
