876.������м���
����һ��ͷ���Ϊ head �ķǿյ���������������м��㡣
����������м��㣬�򷵻صڶ����м��㡣
���룺[1,2,3,4,5]
��������б��еĽ�� 3 (���л���ʽ��[3,4,5])
���صĽ��ֵΪ 3 �� (����ϵͳ�Ըý�����л������� [3,4,5])��
ע�⣬���Ƿ�����һ�� ListNode ���͵Ķ��� ans��������
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, �Լ� ans.next.next.next = NULL.

��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/middle-of-the-linked-list
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������

˼·��
��������б�����ͬʱ����������Ԫ�����η������� A �С�������Ǳ������� N ��Ԫ�أ�
��ô�����Լ�����ĳ���ҲΪ N����Ӧ���м�ڵ㼴Ϊ A[N/2]��

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
        
        
ʱ�临�Ӷȣ�O(N)��N�Ǹ�������Ľ����Ŀ��
�ռ临�Ӷȣ�O(N)������A��ȥ�Ŀռ䡣


˼·����
���ÿ���ָ�뷨��������ָ�� slow �� fast һ���������slow һ����һ����fast һ������������ô�� fast ���������ĩβʱ��slow ��Ȼλ���м䡣
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        first = slow = head
        while first and first.next:
            slow = slow.next
            first = first.next.next
        return low

ʱ�临�Ӷȣ�O(N)��N�Ǹ�������Ľ����Ŀ��
�ռ临�Ӷȣ�O(1)��ֻ��Ҫ�����ռ��� slow �� first ����ָ�롣



