"""103二叉树的锯齿形层序遍历
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


思路：
可设置一双端队列，用于暂存一层的节点。根据当前层是奇数层还是偶数层，决定此队列的读取顺序是从前到后还是从后到前。
另设一flag变量，作用是标记此层的读取顺序，遍历完一层后将flag取反即可。

时间复杂度：O(N)
空间复杂度：O(N)
日期：2021.3.27
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        flag = True
        ans = []
        while queue:
            size = len(queue)
            level_queue = deque()
            for _ in range (size):
                node = queue.popleft()
                if flag:
                    level_queue.append(node.val)
                else:
                    level_queue.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(list(level_queue))
            flag = not flag
        return ans
