# DAA Programming Project
# Spring 2023
# Asfiya Misba - 1002028239
import tkinter as tk
import time
import random

numbers = []


def generate_numbers():
    global numbers  # Declare numbers as a global variable
    array_size = int(entry.get())
    numbers = [random.randint(0, 100) for i in range(array_size)]
    result_label.config(text=f"Generated numbers: {numbers}")


'''
def generate_numbers():
    array_size = int(entry.get())
    numbers = [random.randint(0, 100) for i in range(array_size)]
    result_label.config(text=f"Generated numbers: {numbers}")
'''


class RedBlackNode:
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.root = None

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


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

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


# Function for linear search
def linearSearch(arr, x):
    print(arr)
    print(x)
    pos = None
    start = time.perf_counter()
    for i in range(len(arr)):
        if arr[i] == x:
            pos = i
            return pos + 1
    return -1


# Function for binary search
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


# Create a window
window = tk.Tk()
window.config(bg='lavender')
window.title("DAA Project - Searching Algorithms")
window.geometry("600x400")
window.minsize(600, 400)

finalLabel = tk.Label(window, text="")

size_label = tk.Label(window, text="Enter the size of the array:")
size_label.pack()
entry = tk.Entry(window)
entry.pack()

generate_button = tk.Button(window, text="Generate Numbers", command=generate_numbers)
generate_button.pack()
generate_button.config(bg='pink')

# Add a label for the search element
x_label = tk.Label(window, text="Enter search element:")
x_label.pack()

# Add an entry field for the search element
x_entry = tk.Entry(window)
x_entry.pack()

# Add a listbox for selecting the search algorithm
search_var = tk.StringVar(value="")
search_listbox = tk.Listbox(window, listvariable=search_var)
search_listbox.pack()


# Function to perform search based on the selected option
def search():
    selected_index = search_listbox.curselection()
    # Get the text of the selected item
    selected_item = search_listbox.get(selected_index)

    print('searched clicked')
    print(selected_index)
    print(selected_item)
    # arr_str = arr_entry.get().split()
    # arr = list(map(int, arr_str))
    x = int(x_entry.get())
    print(search_var.get())
    if selected_item == 'Linear Search':
        start = time.perf_counter()
        pos = linearSearch(numbers, x)
        end = time.perf_counter()
        tt = end - start
        if pos != -1:
            finalLabel.configure(text=f"Element found at index {pos}, Time taken = {tt}")
            finalLabel.pack()
        else:
            finalLabel.configure(text=f"Element not found, Time taken = {tt}")
            finalLabel.pack()

    elif selected_item == 'Binary Search':
        numbers.sort()
        start = time.perf_counter()
        pos = binarySearch(numbers, x)
        end = time.perf_counter()
        tt = end - start
        if pos != -1:
            finalLabel.configure(text=f"Element found at index {pos}, Time taken = {tt}")
            finalLabel.pack()
        else:
            finalLabel.configure(text=f"Element not found, Time taken = {tt}")
            finalLabel.pack()

    elif selected_item == 'BST Search':
        bst = BST()
        for element in numbers:
            bst.insert(element)
        start = time.perf_counter()
        pos = bst.BST_Search(x)
        end = time.perf_counter()
        tt = end - start
        if pos:
            finalLabel.configure(text=f"Element {x} found in the BST, Time taken = {tt}")
            finalLabel.pack()
        else:
            finalLabel.configure(text=f"Element {x} not found in the BST, Time taken = {tt}")
            finalLabel.pack()

    elif selected_item == 'Red-Black Search':
        rb = RedBlackTree()
        for element in numbers:
            rb.insert(element)
        start = time.perf_counter()
        pos = rb.RedBlack_Search(x)
        end = time.perf_counter()
        tt = end - start
        if pos:
            finalLabel.configure(text=f"Element {x} found in the Red-Black Tree, Time taken = {tt}")
            finalLabel.pack()
        else:
            finalLabel.configure(text=f"Element {x} not found in the Red-Black Tree, Time taken = {tt}")
            finalLabel.pack()


# Add search options to the listbox
search_listbox.insert(1, "Linear Search")
search_listbox.insert(2, "Binary Search")
search_listbox.insert(3, "BST Search")
search_listbox.insert(4, "Red-Black Search")

# Add a button to perform search
search_button = tk.Button(window, text="Search", command=search)
search_button.pack()
search_button.config(bg='pink')

# Add a label for the search result
result_label = tk.Label(window, text="")
result_label.pack()
finalLabel.pack()
# Start the window
window.mainloop()
