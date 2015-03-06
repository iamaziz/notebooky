
# coding: utf-8

""""
Implementation and running time visualization of six Comparison-Sort Algorithms:
     Bubble sort, Selection sort, Insertion sort, Quicksort, Mergesort, and Heapsort.

By: Aziz Alto
Thanx to: Python Algorithms book (by: Hetland) and Wikipedia.
"""


# Algorithms Implementation

# In[1]:

def bubble_sort(seq):
    """ worst(n^2), best(n), avg(n^2)
        stable: yes
    """
    for passnum in range(len(seq) - 1, 0, -1):
        for i in range(passnum):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]


# In[2]:

def selection_sort(seq):
    """ worst(n^2), best(n^2), avg(n^2)
        stable: no
    """
    for i in range(len(seq) - 1):
        mini, miniat = seq[i], i
        for j in range(i + 1, len(seq)):
            if seq[j] < mini:
                mini, miniat = seq[j], j
        seq[i], seq[miniat] = seq[miniat], seq[i]


# In[3]:

def insertion_sort(seq):
    """ worst(n^2), best(n), avg(n^2)
        stable: yes
    """
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j - 1] > seq[j]:
            seq[j - 1], seq[j] = seq[j], seq[j - 1]
            j -= 1


# In[4]:

def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi


def quicksort(seq):
    """ worst(n^2), best(n lgn), avg(n lgn)
        stable: no
    """
    if len(seq) <= 1:
        return seq
    lo, pi, hi = partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi)


# In[5]:

def mergesort(seq):
    """ worst(n lgn), best(n lgn), avg(n lgn)
        stable: yes
    """
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = mergesort(lft)
    if len(rgt) > 1:
        rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


# In[6]:

def heapify(seq, i, n):
    l, r = 2 * i + 1, 2 * (i + 1)
    maxat = i
    if l <= n and seq[l] > seq[i]:
        maxat = l
    if r <= n and seq[r] > seq[maxat]:
        maxat = r
    if maxat != i:
        seq[i], seq[maxat] = seq[maxat], seq[i]
        heapify(seq, maxat, n)


def buildheap(seq, s, n):
    for i in range(s, -1, -1):
        heapify(seq, i, n)


def heapsort(seq):
    """ worst(n lgn), best(n lgn), avg(n lgn)
        stable: no
    """
    end = len(seq) - 1
    start = end / 2
    buildheap(seq, start, end)

    for i in range(end, 0, -1):
        seq[0], seq[i] = seq[i], seq[0]
        end -= 1
        heapify(seq, 0, end)



# In[2]:

# Running time test and visualization 

from random import randrange
import time
import matplotlib.pyplot as plt
from math import log


def time_test(algorithms, sample_start=100, sample_stop=901, sample_step=100, list_order='random'):

    for algo in algorithms:
        algoname = algo.__name__
        size, period = [], []
        lists = []
        for list_length in range(sample_start, sample_stop, sample_step):            
            list_ = [randrange(1000) for _ in range(list_length)]
            if list_order == 'reversed':
                list_ = [x for x in range(list_length, 0, -1)]
            elif list_order == 'same':
                list_ = [10 for _ in range(list_length)]
            elif list_order == 'sorted':
                list_ = range(list_length)

            lists.append(list_)
            start = time.time()
            algo(list_)
            end = time.time()
            size.append(list_length)
            period.append(end - start)
        analysisdict[algoname] = zip(size, period)


def print_result(d):
    """print out the running times"""
    for k, v in d.items():
        print k
        print("size\ttime")
        for e in v:
            size, time = e
            print size, time

def plot_result(d, list_order):
    """plot the running results"""

    # for plot labels, exchange algo fn name with name and compelxity (in latex)
    notations_labels = [
    ["mergesort", "Merge sort: $O(n\log{n})$ $\Theta(n\log{n})$ $\Omega(n\log{n})$"], 
    ["bubble_sort", "Bubble sort: $O(n^2)$ $\Theta(n^2)$ $\Omega(n)$"],
    ["heapsort", "Heapsort: $O(n\log{n})$ $\Theta(n\log{n})$ $\Omega(n\log{n})$"],
    ["quicksort", "Quicksort: $O(n^2)$ $\Theta(n\log{n})$ $\Omega(n\log{n})$"],
    ["selection_sort", "Selection sort: $O(n^2)$ $\Theta(n^2)$ $\Omega(n^2)$"], 
    ["insertion_sort", "Insertion sort: $O(n^2)$ $\Theta(n^2)$ $\Omega(n)$"]]

    for k in d:
        for n in notations_labels:
            if k == n[0]:
                d[n[1]] = d.pop(k) # replace dict key value

    for k, v in d.items():
        plt.plot(*zip(*v), marker='x', label=k)

    plt.title('Comparison-Sort algorithms compared')
    plt.xlabel('Size of the list (list order: {} values)'.format(list_order.upper()))
    plt.ylabel('Time taken to sort a list (sec)')
    plt.legend(loc=2,prop={'size':11})
    plt.show()




def main(type_='all', start=100,stop=901,step=100, list_order='random'):
    
    if type_ == "all":
        algos = [selection_sort, bubble_sort, mergesort, insertion_sort, quicksort, heapsort]
    elif type_ == "quadratic":
        algos = [selection_sort, bubble_sort, insertion_sort]
    elif type_ == "log-linear":
        algos = [mergesort, heapsort, quicksort]
    else:
        print("unknown input")
        exit(0)

    global analysisdict

    analysisdict = {}
    time_test(algos, start, stop, step, list_order)
    print_result(analysisdict)
    plot_result(analysisdict, list_order)

if __name__ == '__main__':
    
    main(start=100, stop=901, step=100, list_order="random")
    main(type_="quadratic", start=100, stop=901, step=100, list_order="reversed")
    main(type_="log-linear", start=100, stop=901, step=100, list_order="same")
