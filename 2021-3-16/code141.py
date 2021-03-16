"""
141.��������
����һ�������ж��������Ƿ��л���

�����������ĳ���ڵ㣬����ͨ���������� next ָ���ٴε���������д��ڻ��� 
Ϊ�˱�ʾ���������еĻ�������ʹ������ pos ����ʾ����β���ӵ������е�λ�ã������� 0 ��ʼ���� 
��� pos �� -1�����ڸ�������û�л���ע�⣺pos ����Ϊ�������д��ݣ�������Ϊ�˱�ʶ�����ʵ�������

��������д��ڻ����򷵻� true �� ���򣬷��� false ��

ʾ�� 1:

���룺head = [3,2,0,-4], pos = 1
�����true
���ͣ���������һ��������β�����ӵ��ڶ����ڵ㡣

��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/linked-list-cycle
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������


˼·��
��������ָ�룬һ��һ������ָ��ÿ��ֻ�ƶ�һ��������ָ��ÿ���ƶ���������ʼʱ������ָ����λ�� head.
����һ����������ƶ��Ĺ����У���ָ�뷴����׷����ָ�룬��˵��������Ϊ�������������ָ�뽫��������β����������Ϊ��������

ʱ�临�Ӷȣ�O(N),NΪ����Ľڵ���.
�ռ临�Ӷȣ�O(1)
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False



"""
����������ϣ��
˼·��
ʹ�ù�ϣ�����洢�����Ѿ����ʹ��Ľڵ㡣
ÿ�����ǵ���һ���ڵ㣬����ýڵ��Ѿ������ڹ�ϣ���У���˵���������ǻ�����������ͽ��ýڵ�����ϣ���С�
�ظ���һ���̣�ֱ�����Ǳ��������������ɡ�

class Solution:
	def hasCycle(self, head: ListNode) -> bool:
		seen = set()
		while head:
			if head in seen:
				return True
			seen.add(head)
			head = head.next
		return False
ʱ�临�Ӷȣ�O(N)
�ռ临�Ӷ�:O(N)		
"""
