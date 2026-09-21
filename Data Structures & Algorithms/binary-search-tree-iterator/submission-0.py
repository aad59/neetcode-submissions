# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.nums = self.inorderTraversal(root)
        self.idx = 0
        self.length = len(self.nums)

    def next(self) -> int:
        x = self.nums[self.idx]
        self.idx += 1
        return x

    def hasNext(self) -> bool:
        return self.idx != self.length


    def inorderTraversal(self, root: Optional[TreeNode]):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()