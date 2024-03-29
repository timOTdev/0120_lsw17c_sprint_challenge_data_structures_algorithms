class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        stack = [stack]  # LIFO

    def breadth_first_for_each(self, cb):
        queue = [self]  # Add root node to queue, FIFO

        while queue:  # while there's a node in the queue
            discovered_node = queue.pop(0)
            if discovered_node.left:  # if there's a left node, add to queue
                queue.append(discovered_node.left)
            if discovered_node.right:  # if there's a right node, add to queue
                queue.append(discovered_node.right)
            cb(discovered_node.value)  # run the cb on that node

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if value < self.value:
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
