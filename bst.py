# Node Class

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'(Node {self.value})'


class BST:
    def __init__(self, value=None):
        if value:
            self.root = Node(value)
            self.size = 1
        else:
            self.root = None
            self.size = 0

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            self.size += 1
        else:
            current_node = self.root

            while True:
                if value == current_node.value:
                    # we have this value already fam
                    return -1
                elif value > current_node.value:
                    if current_node.right is None:
                        current_node.right = Node(value)
                        self.size += 1
                        break
                    else:
                        current_node = current_node.right
                else:
                    # value < current_node.value
                    if current_node.left is None:
                        current_node.left = Node(value)
                        self.size += 1
                        break
                    else:
                        current_node = current_node.left
    # end of insert()
    def search(self, target):
        # we are only gonna return True if found
        if self.root is None:
            return False
        else:
            current_node = self.root
            while True:
                if current_node is None:
                    return False
                
                if current_node.value == target:
                    return True
                elif target > current_node.value:
                    current_node = current_node.right
                else:
                    current_node = current_node.left
    # end of search()

    def delete(self, target):
        def oneLeftChild(target, parent):
            if target.value > parent.value:
                parent.right = target.left
            else:
                parent.left = target.left
        
        def oneRightChild(target, parent):
            if target.value > parent.value:
                parent.right = target.right
            else:
                parent.left = target.right

        def noChildren(target, parent):
            if target.value > parent.value:
                parent.right = None
            else:
                parent.left = None
        
        def twoChildren(target, parent):
            temp_node = target.right
            temp_parent = target
            while True:
                if temp_node.left != None:
                    temp_parent = temp_node
                    temp_node = temp_node.left
                else:
                    break
            
            if temp_node.right != None:
                temp_parent.left = temp_node.right
            else:
                noChildren(temp_node, temp_parent)

            if target.value > parent.value:
                temp_node.left = target.left
                temp_node.right = target.right
                parent.right = temp_node
            else:
                temp_node.left = target.left
                temp_node.right = target.right
                parent.left = temp_node
            



        if self.root is None:
            return -1
        else:
            current_node = self.root
            parent_node = None
            while True:
                if current_node is None:
                    return False

                if current_node.value == target:
                    if current_node.right == None and current_node.left == None:
                        noChildren(current_node, parent_node)
                        break
                    elif current_node.right == None and current_node.left != None:
                        oneLeftChild(current_node, parent_node)
                        break
                    elif current_node.left == None and current_node.right != None:
                        oneRightChild(current_node, parent_node)
                        break
                    elif current_node.left != None and current_node.right != None:
                        twoChildren(current_node, parent_node)
                        break
                    #both children

                elif target > current_node.value:
                    if target == current_node.right.value:
                        parent_node = current_node
                    current_node = current_node.right
                else:
                    if target == current_node.left.value:
                        parent_node = current_node
                    current_node = current_node.left
        
        
            

    def sort_plz(self):
        # returns a list that is sorted
        def helper(node):
            if node is None:
                return []
            else:
                return helper(node.left) + [node.value] + helper(node.right)

        return helper(self.root)
        
# end of BST class
