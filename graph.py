# DAA Programming Project
# Spring 2023
# Asfiya Misba - 1002028239
import random
import time
import matplotlib.pyplot as plt
from without_gui import *


def generate_random_array(size):
    return [random.randint(0, 1000) for _ in range(size)]


def plot_graph(x, y1, y2, y3, y4):
    plt.plot(x, y1, label='Linear Search')
    plt.plot(x, y2, label='Binary Search')
    plt.plot(x, y3, label='BST Search')
    plt.plot(x, y4, label='Red-Black Tree Search')
    plt.xlabel('Input size')
    plt.ylabel('Execution time (seconds)')
    plt.legend()
    plt.show()


def main():
    sizes = [100, 1000, 10000, 100000]
    linear_times = []
    binary_times = []
    bst_times = []
    rb_times = []
    for size in sizes:
        arr = generate_random_array(size)
        target = random.randint(0, 1000000)

        start_time = time.time()
        linearSearch(arr, target)
        end_time = time.time()
        time_taken = end_time - start_time
        linear_times.append(time_taken)

        start_time1 = time.time()
        binarySearch(arr, target)
        end_time1 = time.time()
        time_taken1 = end_time1 - start_time1
        binary_times.append(time_taken1)

        start_time2 = time.time()
        bst = BST()
        for element in arr:
            bst.insert(element)
        bst.BST_Search(target)
        end_time2 = time.time()
        time_taken2 = end_time2 - start_time2
        bst_times.append(time_taken2)

        start_time3 = time.time()
        rb = RedBlackTree()
        for element in arr:
            rb.insert(element)
        rb.RedBlack_Search(target)
        end_time3 = time.time()
        time_taken3 = end_time3 - start_time3
        rb_times.append(time_taken3)

    plot_graph(sizes, linear_times, binary_times, bst_times, rb_times)


if __name__ == '__main__':
    main()
