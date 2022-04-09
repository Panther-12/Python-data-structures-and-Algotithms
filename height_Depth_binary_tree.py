# Height of a tree is the longest path from a node to a leaf
# max of left and right and add 1
from complex_binary_tree import tree2

def tree_height(node):
    if node is None:
        return 0
    return 1+max(tree_height(node.left),tree_height(node.right))




# size of a binary tree is the max of right plus left plus one
def size_tree(node):
    if node is None:
        return None
    return 1+size_tree(node.left)+ size_tree(node.right)

