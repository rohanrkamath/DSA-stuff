class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Find maxNode
    def maxNode(self):
        if self.root is None:
            print("The tree is empty")
            return

        curr = self.root
        while curr.left:
            curr = curr.left

        return curr.data
    
    # Find MinNode
    def minNode(self):
        if self.root is None:
            print("The tree is empty")
            return

        curr = self.root
        while curr.right:
            curr = curr.right

        return curr.data

    # Add a node
    
    def addNode(self, data, curr_node):
        new_node = Node(data)

        if curr_node.data == data:
            print('BST cannot have duplicate data!')
            return

        if data < curr_node.data:
            if curr_node.left:
                self.addNode(data, curr_node.left)
            else:
                curr_node.left = new_node

        else:
            if curr_node.right:
                self.addNode(data, curr_node.right)
            else:
                curr_node.right = new_node

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.addNode(data, self.root)
        
    
    # Print Traversals - InOrder, PostOrder, PreOrder
    def preOrder(self, curr_node):
    # root -> left -> right
        if curr_node:
            print(str(curr_node.data), end = '-')
            if curr_node.left:
                self.preOrder(curr_node.left)
            if curr_node.right:
                self.preOrder(curr_node.right)

    def inOrder(self, curr_node):
    # left -> root -> right
        if curr_node:
            if curr_node.left:
                self.inOrder(curr_node.left)
            print(str(curr_node.data), end = '-')
            if curr_node.right:
                self.inOrder(curr_node.right)

    def postOrder(self, curr_node):
    # left -> right -> root
        if curr_node:
            if curr_node.left:
                self.postOrder(curr_node.left)
            if curr_node.right:
                self.postOrder(curr_node.right)
            print(str(curr_node.data), end = '-')

    def printTree(self, name):
        if self.root is None:
            print('The tree is empty.')
            return

        temp_node = self.root
        if name == 'preorder':
            self.preOrder(temp_node)
        elif name == 'inorder':
            self.inOrder(temp_node)
        elif name == 'postorder':
            self.postOrder(temp_node)

if __name__ == '__main__':
    tree = BST()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(20)
    tree.insert(8)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)

    ''' The tree created - 
                    10
                 /      \
               5         12
              / \           \
            4     8          20
                 /          /
                7         15
                         /
                       13
    '''
    tree.printTree('preorder')
    
            
            
        
    # Delete a node
    # Find a node

	
