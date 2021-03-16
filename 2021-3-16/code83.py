"""
83.ɾ�����������е��ظ�Ԫ��
����һ����������ɾ�������ظ���Ԫ�أ�ʹ��ÿ��Ԫ��ֻ����һ�Ρ�

ʾ�� 1:

����: 1->1->2
���: 1->2

��Դ��
���ۣ�https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/


˼·��
ָ�� cur ָ��ָ��ͷ�� head
�� cur �� cur.next �Ĵ���Ϊѭ��������������������һ��������ʱ˵������û��ȥ�ظ��ı�Ҫ��
�� cur.val �� cur.next.val ���ʱ˵����Ҫȥ�أ��� cur ����һ��ָ��ָ����һ������һ�����������ܴﵽȥ�ظ���Ч��
���������� cur �ƶ�����һ��λ�ü���ѭ��
ʱ�临�Ӷȣ�O(n)
�ռ临�Ӷȣ�O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur is not None and cur.next is not None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return head
