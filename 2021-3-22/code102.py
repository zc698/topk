code102
102.二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

思路：
用一个二元组 (node, level) 来表示状态，它表示某个节点和它所在的层数，每个新进队列的节点的 level 值都是父亲节点的 level 值加一。最后根据每个点的 level 对点进行分类，分类的时候我们可以利用哈希表，维护一个以 level 为键，对应节点值组成的数组为值，广度优先搜索结束以后按键 level 从小到大取出所有值，组成答案返回即可。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [] # 特殊情况，root为空直接返回
        from collections import deque
        res = []   
        layer = deque()
        layer.append(root)  # 压入初始节点
        while layer:
            cur_layer = []    # 临时变量，记录当前层的节点
            for _ in range(len(layer)):  # 遍历某一层的节点
                node = layer.popleft()   # 将要处理的节点弹出
                cur_layer.append(node.val)
                if node.left:            # 如果当前节点有左右节点，则压入队列，根据题意注意压入顺序，先左后右
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)  
            res.append(cur_layer)        # 某一层的节点都处理完之后，将当前层的结果压入结果集
        return res
        
时间复杂度：O(n)
空间复杂度：O(n)
