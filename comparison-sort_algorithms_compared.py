
# coding: utf-8

# #### Comparison and complexity analysis of six comparison-sort Algorithms:
# - Bubble sort, Selection sort, Insertion sort, Quicksort, Mergesort, and Heapsort.

# In[16]:

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
            if seq[j] < mini: mini, miniat = seq[j], j
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
    if len(seq) <= 1: return seq
    lo, pi, hi = partition(seq)
    return quicksort(lo) + [pi] + quicksort(hi)


# In[5]:

def mergesort(seq):
    """ worst(n lgn), best(n lgn), avg(n lgn)
        stable: yes
    """
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = mergesort(lft)
    if len(rgt) > 1: rgt = mergesort(rgt)
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


# `Last updated: Thu Aug 28 20:54:38 EDT 2014`
# 
# `By: Aziz Alto`
# 
# `Thanx: Python Algorithms, Hetland and Wikipedia.`

# In[2]:

# Test (time complexity)
from random import randrange
import time

def test(algorithms):

    global analysisdict
    
    for algo in algorithms:
        algoname = algo.__name__
        size, period = [], []
        for lstlngth in range(100, 1001, 100):
            lst = [randrange(1000) for _ in range(lstlngth)]
            start = time.time()
            algo(lst)
            end = time.time()
            size.append(lstlngth)
            period.append(end - start)
            
        analysisdict[algoname] = zip(size, period)

if __name__ == '__main__':
    toTest = [selection_sort, bubble_sort, mergesort, insertion_sort, quicksort, heapsort]
    analysisdict = {}
    test(toTest)

# print results
d = analysisdict
for k, v in d.items():
    print k
    print("size\ttime")
    for e in v:
        size, time = e
        print size, time

# plot results
import matplotlib
import matplotlib.pyplot as plt
from math import log

for k, v in d.items():
    plt.plot(*zip(*v), label=k)
    
plt.title('comparison-sort algorithms compared')
plt.xlabel('Size of the list')
plt.ylabel('Time taken to sort the list (sec)')
plt.legend(loc='upper left')
matplotlib.rcParams['savefig.dpi'] =  2 * matplotlib.rcParams['savefig.dpi'] # frame size
plt.show()


# In[7]:

# Test (time complexity)
from random import randrange
import time

def testit(algorithms):

    global analysisdict
    
    for algo in algorithms:
        algoname = algo.__name__
        size, period = [], []
        for lstlngth in range(1000, 10001, 1000):
            lst = [randrange(1000) for _ in range(lstlngth)]
            start = time.time()
            algo(lst)
            end = time.time()
            size.append(lstlngth)
            period.append(end - start)
            
        analysisdict[algoname] = zip(size, period)


# In[10]:

""" Quadratic algorithms """
if __name__ == '__main__':
    toTest = [selection_sort, bubble_sort, insertion_sort]
    analysisdict = {}
    testit(toTest)

# plot results
d = analysisdict
for k, v in d.items():
    plt.plot(*zip(*v), label=k)
    
plt.title('Algorithms with Quadratic running time')
plt.xlabel('Size of the list')
plt.ylabel('Time taken to sort the list (sec)')
plt.legend(loc='upper left')
plt.show()


# In[11]:

""" Loglinear algorithms """
if __name__ == '__main__':
    toTest = [mergesort, heapsort, quicksort]
    analysisdict = {}
    testit(toTest)

# plot results
d = analysisdict
for k, v in d.items():
    plt.plot(*zip(*v), label=k)
    
plt.title('Algorithms with Loglinear running time')
plt.xlabel('Size of the list')
plt.ylabel('Time taken to sort the list (sec)')
plt.legend(loc='upper left')
plt.show()


# In[8]:

# Test (time complexity)
""" Reversed List """

def test_reverse(algorithms):

    global analysisdict
    
    for algo in algorithms:
        algoname = algo.__name__
        size, period = [], []
        for lstlngth in range(100, 901, 100):
            lst = [x for x in range(lstlngth, 0, -1)]
            start = time.time()
            algo(lst)
            end = time.time()
            size.append(lstlngth)
            period.append(end - start)
        analysisdict[algoname] = zip(size, period)


# In[9]:

""" Quadratic algorithms with reversed list """
if __name__ == '__main__':
    toTest = [selection_sort, bubble_sort, insertion_sort]
    analysisdict = {}
    test_reverse(toTest)

# plot results
d = analysisdict
for k, v in d.items():
    plt.plot(*zip(*v), label=k)
    
plt.title('Quadratic algorithms with reversed list')
plt.xlabel('Size of the list')
plt.ylabel('Time taken to sort the list (sec)')
plt.legend(loc='upper left')
plt.show()


# In[15]:

""" Loglinear algorithms with reversed list """
if __name__ == '__main__':
    toTest = [mergesort, heapsort, quicksort]
    analysisdict = {}
    test_reverse(toTest)

# plot results
d = analysisdict
for k, v in d.items():
    plt.plot(*zip(*v), label=k)
    
plt.title('Loglinear algorithms with reversed list')
plt.xlabel('Size of the list')
plt.ylabel('Time taken to sort the list (sec)')
plt.legend(loc='upper left')
plt.show()


# In[13]:

# Test (time complexity)
""" Same element List """
from random import randrange
import time

def test_same(algorithms):

    global analysisdict
    
    for algo in algorithms:
        algoname = algo.__name__
        size, period = [], []
        for lstlngth in range(100, 901, 100):
            lst = [10 for _ in range(lstlngth)]
            start = time.time()
            algo(lst)
            end = time.time()
            size.append(lstlngth)
            period.append(end - start)
        analysisdict[algoname] = zip(size, period)


# In[14]:

""" Loglinear algorithms with all elements in list are same value """
if __name__ == '__main__':
    toTest = [mergesort, heapsort, quicksort]
    analysisdict = {}
    test_same(toTest)

# plot results
d = analysisdict
for k, v in d.items():
    plt.plot(*zip(*v), label=k)
    
plt.title('Loglinear algorithms with same-element list')
plt.xlabel('Size of the list')
plt.ylabel('Time taken to sort the list (sec)')
plt.legend(loc='upper left')
plt.show()


                By: Aziz Alto, Thu May 15 15:32:40 EDT 2014
                