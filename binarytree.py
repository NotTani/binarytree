class BinarySearchTree:

    # This is a Node class that is internal to the BinarySearchTree class.
    class __Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

        def __repr__(self):
            return f"Node({self.val}, l={self.left}, r={self.right})"

        def getVal(self):
            return self.val

        def setVal(self, newVal):
            self.val = newVal

        def getLeft(self):
            return self.left

        def getRight(self):
            return self.right

        def setLeft(self, newLeft):
            self.left = newLeft

        def setRight(self, newRight):
            self.right = newRight

        # This method should iterate over the left side of the tree, then
        # return the val, then iterate over the right side of the tree.
        def __iter__(self):
            if self.left is not None:
                for i in self.left:
                    yield i

            yield self.val

            if self.right is not None:
                for i in self.right:
                    yield i

    def __init__(self):
        self.root = None

    def __repr__(self):
        return f"Tree({repr(self.root)})"

    # Insert something into the tree.
    def insert(self, val)

        # The __insert function is recursive and is not passed a self
        # parameter. It is static function (not a method of the class) but
        # is hidden inside so users of the class will not know it exists.
        def __insert(root, val):
            # TODO: implement this
            pass

        self.root = __insert(self.root, val)

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()

def main():
    s = input("Enter a list of numbers, seperated by spaces: ")
    lst = s.split()

    tree = BinarySearchTree()
    for x in lst:
        tree.insert(float(x))

    for x in tree:
        print(x)

if __name__ == "__main__":
    main()
