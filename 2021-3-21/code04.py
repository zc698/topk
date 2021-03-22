面试题 04.04. 检查平衡性
实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。
思路：自顶向下递归
对于当前遍历到的节点，首先计算左右子树的高度，如果左右子树的高度差是否不超过1，再分别递归地遍历左右子节点，并判断左子树和右子树是否平衡。

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

方法2：
思路：自底向上
对于当前遍历到的节点，先递归地判断其左右子树是否平衡，再判断以当前节点为根的子树是否平衡。
如果一棵子树是平衡的，则返回其高度（高度一定是非负整数），否则返回−1。
如果存在一棵子树不平衡，则整个二叉树一定不平衡。

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def Height(root:TreeNode) -> int:
            if not root:
                return 0
            leftHeight = Height(root.left)
            rightHeight = Height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) >1:
                return -1
            else:
                return max(leftHeight,rightHeight) + 1

        return Height(root) >= 0
        
        
时间复杂度：O(n)
空间复杂度：O(n)




