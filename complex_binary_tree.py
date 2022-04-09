# create the following binary tree

# class to create a node
class TreeNode:
    def __init__(self,key):
        self.key= key
        self.right = None
        self.left = None

# convinient solution write a method which converts a tuple to a tree
# The middle item represents the root node

def parse_tree(data):
    # check if data is a tuple and qualifies to form a tree
    # The root node is set to the middle element and a recursive call is applied
    # to perform the same operation to the right and left branches
    if isinstance(data,tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tree(data[0])
        node.right = parse_tree(data[2])
    elif data is None:
        node = None
    # Terminating condition of the recursive function
    else:
        node = TreeNode(data)
    return node

# visualize the binary tree
def display_tree(node, space='\t', level=0):
    # if the node is none
    if node is None:
        print(space*level+'@')
        return 

    # if node is a leaf
    if node.right is None and node.left is None:
        print(space*level+str(node.key))
        return

    # if the node has children
    display_tree(node.right,space,level+1)
    print(space*level+str(node.key))
    display_tree(node.left,space,level+1)

tree2 = parse_tree(((1,3,None),2,((None,3,4),5,(6,7,8))))


display_tree(node=tree2)
# ASSIGNMENT ########

# write a function to return a tree to a tuple
# how postorder works

# BINARY TREE TRAVERSAL ########
#- Visiting the keys once
# ------Types-------
#      1. inorder
#      2. preorder
#      3. postorder

# in order traversal
# traverse the left side, get to the root node, traverse the right side
def traverse_in_order(node):
    if node is None:
        return []
    return traverse_in_order(node.left)+[node.key]+traverse_in_order(node.right)

traverse_in_order(tree2)


# preorder traversal
# Start with the root node, traverse the left-side, traverse the right side
keys = []
def traverse_pre_order(node):
    if node is None:
        return []
    return [node.key]+traverse_pre_order(node.left)+traverse_pre_order(node.right) 


traverse_pre_order(tree2)
print(keys)

# postorder traversal 
# traverse the left print , root, traverse the right node
def traverse_post_order(node):
    if node is None:
        return []
    return traverse_post_order(node.left)+traverse_post_order(node.right)+[node.key]    