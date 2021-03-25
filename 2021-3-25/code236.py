236.�������������������
����һ��������, �ҵ�����������ָ���ڵ������������ȡ�

�ٶȰٿ�������������ȵĶ���Ϊ���������и��� T �������ڵ� p��q������������ȱ�ʾΪһ���ڵ� x������ x �� p��q �������� x ����Ⱦ����ܴ�һ���ڵ�Ҳ���������Լ������ȣ���

���룺root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
�����3
���ͣ��ڵ� 5 �ͽڵ� 1 ��������������ǽڵ� 3 ��

2021.3.25
��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������

˼·��
ͨ���ݹ�Զ��������к����������Խ��Ҷ�ڵ㣬����null,��root����p,q����root.

ʱ�临�Ӷȣ�O(n),nΪ�������Ľڵ�����
�ռ临�Ӷȣ�O(n)��nΪ�������Ľڵ�����

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left and not right:
            return 
        if not left:
            return right
        if not right:
            return left
        return root
