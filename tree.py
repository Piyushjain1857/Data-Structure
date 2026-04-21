# ============================================
# BINARY SEARCH TREE (BST)
# BCA AI & DS — Unit 4
# ============================================

class Node:
    def __init__(self, data):
        self.data  = data   # value stored in node
        self.left  = None   # left child
        self.right = None   # right child

class BST:
    def __init__(self):
        self.root = None   # empty tree

    # ---------- INSERT ----------
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)          # first node becomes root
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:                # go LEFT if smaller
            if node.left is None:
                node.left = Node(data)      # empty spot found
            else:
                self._insert(node.left, data)
        elif data > node.data:              # go RIGHT if larger
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)
        # if data == node.data, we ignore duplicates

    # ---------- SEARCH ----------
    def search(self, data):
        return self._search(self.root, data)

    def _search(self, node, data):
        if node is None:                    # reached end, not found
            return False
        if data == node.data:               # found it!
            return True
        elif data < node.data:              # search left
            return self._search(node.left, data)
        else:                               # search right
            return self._search(node.right, data)

    # ---------- DELETE ----------
    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return node                     # node not found

        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:                               # found the node to delete
            # Case 1: No children (leaf node)
            if node.left is None and node.right is None:
                return None

            # Case 2: One child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Case 3: Two children
            # Find in-order successor (smallest in right subtree)
            else:
                successor = self._min_node(node.right)
                node.data = successor.data  # replace with successor
                node.right = self._delete(node.right, successor.data)

        return node

    def _min_node(self, node):
        while node.left is not None:
            node = node.left                # go all the way left
        return node

    # ---------- INORDER TRAVERSAL (gives sorted output) ----------
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)   # Left
            result.append(node.data)           # Root
            self._inorder(node.right, result)  # Right


# ---- TESTING THE BST ----
bst = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

print("Inorder (sorted):", bst.inorder())   # [20,30,40,50,60,70,80]
print("Search 40:", bst.search(40))          # True
print("Search 99:", bst.search(99))          # False
bst.delete(30)
print("After deleting 30:", bst.inorder())   # [20,40,50,60,70,80]