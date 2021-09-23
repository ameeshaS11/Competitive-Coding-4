#Time Complexity : O(n)
#Space Complexity : O(1) 
# Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root == None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(right-left)>1:
            return -1
        if left== -1 or right == -1:
            return -1
        return max(right, left)+1
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if self.height(root) == -1:
            return False
        else:
            return True