# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        layer_tree = [[root]]
        line_node = [root]
        line = 0
        target_line = -1
        while line_node:
            line += 1
            temp_line = []
            while line_node:
                node = line_node.pop()
                if node is target:
                    target_line == line
                if node.left:
                    temp_line.append(node.left)
                if node.right:
                    temp_line.append(node.right)
            line_node = temp_line.copy()
            layer_tree.append(temp_line)
        result = []
        if target_line + K <= line:
            for i in layer_tree[target_line + K]:
                if i is not target:
                    result.append(i.val)
        if abs(target_line - K) <= line:
            for i in layer_tree[abs(target_line - K)]:
                if i is not target:
                    result.append(i.val)
        return result

t3 = TreeNode(3)
t5 = TreeNode(5)
t1 = TreeNode(1)
t6 = TreeNode(6)
t2 = TreeNode(2)
t0 = TreeNode(0)
t8 = TreeNode(8)
t7 = TreeNode(7)
t4 = TreeNode(4)
t3.right = t1
t3.left = t5
t5.left = t6
t5.right = t2
t1.left = t0
t1.right = t8
t2.right = t4
t2.left = t7
s = Solution()
result = s.distanceK(t3, t5, 2)
print(result)


