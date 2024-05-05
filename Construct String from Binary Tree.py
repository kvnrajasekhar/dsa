#link : https://leetcode.com/problems/construct-string-from-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def pre(node,string=""):
            if node is None:
                return ""
            string += str(node.val)
            if node.left is not None or node.right is not None:
                string += "(" + pre(node.left) + ")"
                if node.right is not None:
                    string += "(" + pre(node.right) + ")" 
            return string
        return pre(root)
