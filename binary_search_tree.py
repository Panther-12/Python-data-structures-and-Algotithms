# The left subtree of any node should only contain nodes with keys less than the current node
# The right subtree of any node should only contain nodes with keys greater than the current node


class Node:
    def __init__(self,key):
        self.key,self.right,self.left = key,None,None

    @staticmethod
    def parse_tree(data):
        if data is None:
            return None
        elif isinstance(data,tuple) and len(data) == 3:
            node = Node(data[1])
            node.left = Node.parse_tree(data[0])
            node.right = Node.parse_tree(data[2])
        else:
            node = Node(data)
        return node

    # traverse in order
    def traverse_in_order(self):
        if self is None:
            return []
        return (Node.traverse_in_order(self.left)+[self.key]+Node.traverse_in_order(self.right))

    # the height of the tree
    def height_tree(self):
        if self is None:
            return None
        return 1+max(self.left,self.right)

    # The size of the tree
    def size_tree(self):
        if self is None:
            return None
        return 1+Node.size_tree(self.left)+Node.size_tree(self.right)

    # check if the tree is a bst
    # returns true and two other parameters: max and min value
    def is_bst(node):
        if node is None:
            return True, None,None
        
    # represent the tree created
    def __str__(self):
        return 'Binary tree <{}>'.format(Node)

tree = ((2,4,7),5,(1,6,8))
tree2 = Node.parse_tree(tree)
print(tree2.right.left.key)