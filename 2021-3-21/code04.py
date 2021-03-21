面试题 04.04. 检查平衡性
实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。
思路：自顶向下递归
对于当前遍历到的节点，首先计算左右子树的高度，如果左右子树的高度差是否不超过 11，再分别递归地遍历左右子节点，并判断左子树和右子树是否平衡。

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
        
        
时间复杂度：O(n^2)
空间复杂度：O(n)
