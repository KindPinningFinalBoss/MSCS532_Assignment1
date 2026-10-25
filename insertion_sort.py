"""
Insertion Sort (monotonically decreasing order).

MSCS-532 Assignment 1. This is the Insertion Sort from Chapter 2 of
Cormen et al., Introduction to Algorithms (4th ed.), with one change: the
comparison in the inner loop is flipped so the array ends up sorted from
largest to smallest instead of smallest to largest.
"""


def insertion_sort_desc(arr):
    """Sort a list in place into monotonically decreasing order.

    Walks from the second element to the end. For each element (the "key"),
    it slides every earlier element that is SMALLER than the key one slot to
    the right, then drops the key into the gap. Sliding the smaller ones back
    is what puts the larger values up front.

    Returns the same list so it can also be used inline.
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        # CLRS uses arr[i] > key here for increasing order. Using < instead
        # moves smaller elements right, so the larger ones lead.
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr
