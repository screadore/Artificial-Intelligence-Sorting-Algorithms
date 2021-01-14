# Quick Sort performs significantly faster than merge sort and rarely reaches its worst case complexity of O(n²) and has 3 main steps.

# 1) We first select an element which we will call the pivot from the array.

# 2) Move all elements that are smaller than the pivot to the left of the pivot; move all elements that are larger than the pivot to the right of the pivot. This is called the partition operation.

# 3) Recursively apply the above 2 steps separately to each of the sub-arrays of elements with smaller and bigger values than the last pivot.

def partition(array, begin, end):
    pivot_idx = begin
    for i in xrange(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot_idx += 1
            array[i], array[pivot_idx] = array[pivot_idx], array[i]
    array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
    return pivot_idx


def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return
    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx - 1)
    quick_sort_recursion(array, pivot_idx + 1, end)


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    return quick_sort_recursion(array, begin, end)