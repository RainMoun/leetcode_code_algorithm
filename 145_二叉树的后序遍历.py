# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.post_order = []

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        '''递归解法
        if not root:
            return []
        if root.left:
            self.postorderTraversal(root.left)
        if root.right:
            self.postorderTraversal(root.right)
        self.post_order.append(root.val)
        return self.post_order
        '''
        if not root:
            return []
        stack = [root]
        stack_2 = []
        while stack:
            node = stack.pop()
            stack_2.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while stack_2:
            self.post_order.append(stack_2.pop().val)
        return self.post_order


s = Solution()
v1 = TreeNode(1)
v2 = TreeNode(2)
v3 = TreeNode(3)
v1.right = v2
v2.left = v3
print(s.postorderTraversal(v1))
