#link : https://leetcode.com/problems/binary-tree-inorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root:Optional[TreeNode],l):
            if root == None:
                return None
            inorder(root.left,l)
            l.append(root.val)
            inorder(root.right,l)
            return l
        l = []
        ans = inorder(root,l)
        return ans


        
        
