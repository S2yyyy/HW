# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        visit=collections.deque()
        visit.append(root)
        ans=[]
        while len(visit)!=0:
            nex=[]
            vals=[]
            for node in visit:
                vals.append(node.val)
                if node.left:
                    nex.append(node.left)
                if node.right:
                    nex.append(node.right)
            ans.append(vals)
            visit=nex
        return ans
            
            
