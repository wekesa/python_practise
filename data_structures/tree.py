class Node:
    def __init__(self, data):
       self.left = None
       self.right = None
       self.data = data

    def insert(self, data):
        if self.data:
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            elif data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
        else:
            self.data = data

    def find_value(self, value):
        if value > self.data:
            if self.right is None:
                print("Value not found")
            else:
                self.right.find_value(value)
        elif value < self.data:
            if self.left is None:
                print("Value not found")
            else:
                self.left.find_value(value)
        else:
            print(value + "Found")

    def in_order_traversal(self, root):
        """
        Traversal : Left -> root -> right
        :param root:
        :return:
        """
        res = []
        if root:
            res = self.in_order_traversal(root.left)
            res.append(root.data)
            res = res + self.in_order_traversal(root.right)

        return res

    def pre_order_traversal(self, root):
        """
        Traversal: root -> left -> right
        :param root:
        :return:
        """
        result = []
        if root:
            result.append(root.data)
            result = result + self.pre_order_traversal(root.left)
            result = result + self.pre_order_traversal(root.right)
        return result

    def post_order_traversal(self, root):
        """
        Traversal: left -> right -> root
        :param root:
        :return:
        """
        res = []
        if root:
            res = self.post_order_traversal(root.left)
            res = res + self.post_order_traversal(root.right)
            res.append(root.data)
        return res


    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

# Driver Code
node = Node(20)
node.insert(14)
node.insert(15)
node.insert(5)
node.print_tree()