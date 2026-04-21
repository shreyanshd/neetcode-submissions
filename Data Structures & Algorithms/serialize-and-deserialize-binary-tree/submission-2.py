# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    DELIMITER = ","
    NULL = "null"

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return self.NULL
        serialized = (
            str(root.val) + self.DELIMITER + 
            self.serialize(root.left) + self.DELIMITER + 
            self.serialize(root.right)
        )
        return serialized
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split(self.DELIMITER)
        self.nodes = []
        for t in tokens:
            if t == self.NULL:
                self.nodes.append(None)
            else:
                self.nodes.append(int(t))
        self.idx = 0

        def preorder():
            if self.idx >= len(self.nodes):
                return None

            val = self.nodes[self.idx]
            self.idx += 1
            
            if val is None:
                return None

            root = TreeNode(val)
            root.left = preorder()
            root.right = preorder()
            return root

        return preorder()