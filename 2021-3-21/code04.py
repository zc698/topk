������ 04.04. ���ƽ����
ʵ��һ�����������������Ƿ�ƽ�⡣����������У�ƽ�����Ķ������£�����һ���ڵ㣬�����������ĸ߶Ȳ���� 1��
˼·���Զ����µݹ�
���ڵ�ǰ�������Ľڵ㣬���ȼ������������ĸ߶ȣ�������������ĸ߶Ȳ��Ƿ񲻳��� 11���ٷֱ�ݹ�ر��������ӽڵ㣬���ж����������������Ƿ�ƽ�⡣

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def Height(root:TreeNode) -> int:
            if not root:
                return 0
            return max(Height(root.left),Height(root.right)) + 1
        if not root:
            return True
        return abs(Height(root.left) - Height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
ʱ�临�Ӷȣ�O(n^2)
�ռ临�Ӷȣ�O(n)
