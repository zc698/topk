code102
102.�������Ĳ������
����һ�������������㷵���䰴 ������� �õ��Ľڵ�ֵ�� �������أ������ҷ������нڵ㣩��
��������[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
�����������������

[
  [3],
  [9,20],
  [15,7]
]

��Դ�����ۣ�LeetCode��
���ӣ�https://leetcode-cn.com/problems/binary-tree-level-order-traversal
����Ȩ������������С���ҵת������ϵ�ٷ���Ȩ������ҵת����ע��������

˼·��
��һ����Ԫ�� (node, level) ����ʾ״̬������ʾĳ���ڵ�������ڵĲ�����ÿ���½����еĽڵ�� level ֵ���Ǹ��׽ڵ�� level ֵ��һ��������ÿ����� level �Ե���з��࣬�����ʱ�����ǿ������ù�ϣ��ά��һ���� level Ϊ������Ӧ�ڵ�ֵ��ɵ�����Ϊֵ������������������Ժ󰴼� level ��С����ȡ������ֵ����ɴ𰸷��ؼ��ɡ�
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [] # ���������rootΪ��ֱ�ӷ���
        from collections import deque
        res = []   
        layer = deque()
        layer.append(root)  # ѹ���ʼ�ڵ�
        while layer:
            cur_layer = []    # ��ʱ��������¼��ǰ��Ľڵ�
            for _ in range(len(layer)):  # ����ĳһ��Ľڵ�
                node = layer.popleft()   # ��Ҫ����Ľڵ㵯��
                cur_layer.append(node.val)
                if node.left:            # �����ǰ�ڵ������ҽڵ㣬��ѹ����У���������ע��ѹ��˳���������
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)  
            res.append(cur_layer)        # ĳһ��Ľڵ㶼������֮�󣬽���ǰ��Ľ��ѹ������
        return res
        
ʱ�临�Ӷȣ�O(n)
�ռ临�Ӷȣ�O(n)
