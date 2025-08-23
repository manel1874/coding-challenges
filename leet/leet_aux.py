from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    """
    From a level-order representation of a binary tree, to 
    a tree object.
    """
    def lor2tree(lor):
        if not lor:
            return None
        
        root = TreeNode(lor[0])
        queue = deque([root])
        i=1
        
        while i < len(lor) and queue:
            current_node = queue.popleft()

            if lor[i] is not None:
                current_node.left = TreeNode(lor[i])
                queue.append(current_node.left)
            i += 1

            if i < len(lor) and lor[i] is not None:
                current_node.right = TreeNode(lor[i])
                queue.append(current_node.right)
            i += 1

        return root
    


if __name__ == "__main__":
    lor_arr = [1,2,3,4,None,2,4,None,None,4]
    root = TreeNode.lor2tree(lor_arr)
    print(root.right.left.right)
    