import queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.lst = []

    def preorderTraversal_digui(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        self.lst.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.lst

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result_lst = []
        stack = []
        while root or stack:
            while root:
                result_lst.append(root.val)
                stack.append(root)
                root = root.left
            if stack:
                root = stack.pop().right
        return result_lst


t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t1.right = t2
t2.right = t3
s = Solution()
result = s.preorderTraversal(t1)
print(result)