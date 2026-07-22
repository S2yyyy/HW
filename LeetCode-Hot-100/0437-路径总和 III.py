# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pre_sum=defaultdict(int)
        pre_sum[0]=1
        ans=0
        def dfs(node:Optional[TreeNode],pre,pre_sum):
            nonlocal ans
            if node is None:
                return
            pre+=node.val
            ans+=pre_sum[pre-targetSum]
            new_pre_sum=pre_sum.copy()
            new_pre_sum[pre]=pre_sum.get(pre,0)+1
            dfs(node.left,pre,new_pre_sum)
            dfs(node.right,pre,new_pre_sum)
        dfs(root,0,pre_sum)
        return ans
