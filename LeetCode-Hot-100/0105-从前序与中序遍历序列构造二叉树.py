# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index={x:i for i,x in enumerate(inorder)}
        def dfs(preorder,inorder,index):
            if not preorder:
                return None
            left_size=index[preorder[0]]-index[inorder[0]]
            left=dfs(preorder[1:1+left_size],inorder[:left_size],index)
            right=dfs(preorder[1+left_size:],inorder[1+left_size:],index)
            return TreeNode(preorder[0],left,right)
        return dfs(preorder,inorder,index)
