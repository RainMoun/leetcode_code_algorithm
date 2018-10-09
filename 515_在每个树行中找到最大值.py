# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result_max =[]
        line_node = [root]
        while line_node:
            value_line = []
            temp_line_son = []
            while line_node:
                node = line_node.pop()
                value_line.append(node.val)
                if node.left:
                    temp_line_son.append(node.left)
                if node.right:
                    temp_line_son.append(node.right)
            print(value_line)
            result_max.append(max(value_line))
            line_node = temp_line_son.copy()
        return result_max

t1 = TreeNode(1)
t2 = TreeNode(3)
t3 = TreeNode(2)
t4 = TreeNode(5)
t5 = TreeNode(3)
t6 = TreeNode(9)
t1.right = t3
t1.left = t2
t2.left = t4
t2.right = t5
t3.right = t6
s = Solution()
result = s.largestValues(t1)
print(result)
