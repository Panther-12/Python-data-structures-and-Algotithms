# Here the tree is traversed based on levels
# The best implementation is to traverse the current node
# store its child nodes in a queue and then traverse them in order

from complex_binary_tree import tree2

def breadth_first_traversal(node):
    # create a queue and store the root node
    q = []
    index = 0
    q.append(node)

    # repeat the operations till all nodes are visited
    # picks the root node and visits it
    # then moves on to the left and right subtrees
    while q is not None and q != '':
        data = q[index]
        print(data.key)

        if data.left is not None:
            q.append(data.left)
        if data.right is not None:
            q.append(data.right)
        q.pop(0)
        index +=1

tree = breadth_first_traversal(tree2)

