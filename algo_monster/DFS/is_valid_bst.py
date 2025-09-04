"""

"""


from aux import TreeNode

class Solution:
    def is_valid_bst(self, root: TreeNode) -> bool:
        
        def dfs(node: TreeNode, minimum: int, maximum: int):
            if node is None:
                return True
            
            valid = (node.val > minimum and node.val < maximum)
            if not valid:
                return False

            return dfs(node.left, minimum, node.val) and dfs(node.right, node.val, maximum)

        return dfs(root, float("-inf"), float("inf"))
    

if __name__ == "__main__":
    lor = [2,1,3]
    root = TreeNode.lor2tree(lor)
    b = Solution().is_valid_bst(root)
    print(b)

    lor = [5,1,4,None,None,3,6]
    root = TreeNode.lor2tree(lor)
    b = Solution().is_valid_bst(root)
    print(b)