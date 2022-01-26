# The root node has various nodes containing user data
# The end nodes with no data are called leaves
# Works for sorted items whereby the left has keys lexical graphically smaller than the root node and
# the right side keys lexical graphically greater than root node
# --- In this case it is called a binary search tree
# --- suitable for representation of collection of data eg Dictionary data


####### PROPERTIES #############
        # key(username) and value(user class object)
        # Binary search tree
        # Balanced tree - it does not skew heavily to the left or right
            # In a balanced tree the number of nodes in each level is twice those of the previous node
            # height of tree(k) = log(N) + 1


## simple binary tree
# The class rep a single node with left and right branches
# The key is the identity of the node
class Treenode:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None


# Call an instance of the class to create a node
node0 = Treenode(0)
node1 = Treenode(1)
node2 = Treenode(2)

# Set the left and right branches of the first node 0 to node 1 and 2
node0.right = node1
node0.left = node2

# Assign the root node to a tree variable
tree = node0

