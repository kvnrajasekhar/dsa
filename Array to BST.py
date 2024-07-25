# lnk : https://www.geeksforgeeks.org/problems/array-to-bst4443/1

class Solution:
    def sortedArrayToBST(self, nums):
        n = len(nums)
        def helper(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            root = Node(nums[m])
            root.left = helper(l, m - 1)
            root.right = helper(m + 1, r)
            return root
        return helper(0, n - 1)
