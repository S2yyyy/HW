# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node:Optional[TreeNode]):
            if node is None:
                return -1
            left_depth=dfs(node.left)+1
            right_depth=dfs(node.right)+1
            nonlocal ans
            ans=max(ans,left_depth+right_depth)
            return max(left_depth,right_depth)
        dfs(root)
        return ans
