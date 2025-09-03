"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 

Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104

https://leetcode.com/problems/subtree-of-another-tree/
"""

from aux import TreeNode

class Solution:
    def is_subtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        def same(node, subnode):

            if node is None and subnode is None:
                return True
            
            if node and subnode and node.val == subnode.val:
                left_is_subtree = same(node.left, subnode.left)
                right_is_subtree = same(node.right, subnode.right)
                return left_is_subtree and right_is_subtree
            else:
                return False

        if subRoot is None:
            return True
        if root is None:
            return False
        
        if same(root, subRoot):
            return True
        
        return self.is_subtree(root.left, subRoot) or self.is_subtree(root.right, subRoot)

    

if __name__ == "__main__":
    root = [3,4,5,1,2]
    subRoot = [4,1,2]
    root = TreeNode.lor2tree(root)
    subRoot = TreeNode.lor2tree(subRoot)
    b = Solution().is_subtree(root, subRoot)
    print(b)

