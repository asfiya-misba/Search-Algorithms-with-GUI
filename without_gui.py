# DAA Programming Project
# Spring 2023
# Asfiya Misba - 1002028239

import sys
import time


# Class to define the node of the red-black tree
class RedBlackNode:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


# Red - Black Tree
class RedBlackTree:
    def __init__(self):
        self.root = None

    # To insert the elements into the red-black tree
    def insert(self, value, curr=None):
        node = RedBlackNode(value, "RED")
        parent = None
        curr = self.root
        while curr is not None:
            parent = curr
            if node.value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        node.parent = parent
        if parent is None:
            self.root = node
        elif node.value < parent.value:
            parent.left = node
        else:
            parent.right = node
        self.balance(node)

    # To balance the red-black tree by performing rotations
    def balance(self, node):
        while node.parent is not None and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle is not None and uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)
        self.root.color = "BLACK"

    # To perform left rotation
    def left_rotate(self, node):
        right = node.right
        node.right = right.left
        if right.left is not None:
            right.left.parent = node
        right.parent = node.parent
        if node.parent is None:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right
        right.left = node
        node.parent = right

    # To perform right rotation
    def right_rotate(self, node):
        left = node.left
        node.left = left.right
        if left.right is not None:
            left.right.parent = node
        left.parent = node.parent
        if node.parent is None:
            self.root = left
        elif node == node.parent.right:
            node.parent.right = left
        else:
            node.parent.left = left
        left.right = node
        node.parent = left

    # To perform the search operation
    def RedBlack_Search(self, value, node=None):
        node = self.root
        while node is not None:
            if node.value == value:
                return node
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return None


# to define the node of the BST
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# BST
class BST:
    def __init__(self):
        self.root = None

    # to insert the elements into the BST
    def insert(self, value, current_node=None):
        if current_node is None:
            current_node = self.root
        if self.root is None:
            self.root = BSTNode(value)
        elif current_node is None:
            current_node = BSTNode(value)
        elif value < current_node.value:
            if current_node.left is None:
                current_node.left = BSTNode(value)
            else:
                self.insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = BSTNode(value)
            else:
                self.insert(value, current_node.right)
        else:
            print("Value already exists in the BST")

    # to perform search
    def BST_Search(self, value, node=None):
        node = self.root
        while node is not None:
            if node.value == value:
                return node
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return None


# linear search
def linearSearch(arr, x):
    pos = None
    for i in range(len(arr)):
        if arr[i] == x:
            pos = i
    if pos:
        # print('Element found at position {}'.format(pos + 1))
        return pos + 1
    else:
        # print('Element not found')
        return -1


# binary search
def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    while (True):
        print('Enter your choice: ')
        ch = int(input(
            '1. Linear Search\t2. Binary Search\t3. Binary Search Tree\t4. Red-Black Tree\t5. Exit\n'))
        if ch == 1:
            n = int(input('Enter the number of elements in the array: '))
            a = input('Enter the array elements: ')
            arr = [int(i) for i in a.split(" ")]
            x = int(input('Enter the element to be searched: '))
            start = time.perf_counter()
            pos = linearSearch(arr, x)
            end = time.perf_counter()
            if pos != -1:
                print('Element found at position {}'.format(pos))
            else:
                print('Element not found')
            print('Time taken = {}'.format(end - start))

        elif ch == 2:
            n = int(input('Enter the number of elements in the array: '))
            a = input('Enter the array elements in a sorted order: ')
            arr = [int(i) for i in a.split(" ")]
            x = int(input('Enter the element to be searched: '))
            start = time.perf_counter()
            pos = binarySearch(arr, x)
            end = time.perf_counter()
            if pos != -1:
                print('Element found at position {}'.format(pos))
            else:
                print('Element not found')
            print('Time taken = {}'.format(end - start))
        elif ch == 3:
            bst = BST()
            n = int(input('Enter the number of elements in the BST: '))
            a = input('Enter the elements of the BST : ')
            arr = [int(i) for i in a.split(" ")]
            x = int(input('Enter the element to be searched: '))
            for element in arr:
                bst.insert(element)
            start = time.perf_counter()
            res = bst.BST_Search(x)
            end = time.perf_counter()
            # print(res)
            if res:
                print('Element {} found in the BST'.format(x))
            else:
                print('Element {} not found in the BST'.format(x))
            print('Time taken = {}'.format(end - start))
        elif ch == 4:
            redblack = RedBlackTree()
            n = int(input('Enter the number of elements in the red-black tree: '))
            a = input('Enter the elements of the red-black tree: ')
            arr = [int(i) for i in a.split(" ")]
            x = int(input('Enter the element to be searched: '))
            for element in arr:
                redblack.insert(element)
            start = time.perf_counter()
            node = redblack.RedBlack_Search(x)
            end = time.perf_counter()
            # print(node)
            if node:
                print("Element {} found in the red-black tree".format(x))
            else:
                print("Element {} not found in the red-black tree".format(x))
            print('Time taken = {}\n'.format(end - start))
        elif ch == 5:
            sys.exit()
        else:
            print('Invalid Choice')
