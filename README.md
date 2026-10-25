# MSCS532_Assignment1

Insertion Sort in Python, sorting into **monotonically decreasing** order.

Assignment 1 for MSCS-532 (Algorithms and Data Structures). The algorithm
follows the Insertion Sort pseudocode from Chapter 2 of *Introduction to
Algorithms* (Cormen, Leiserson, Rivest, & Stein, 4th ed.), with the inner-loop
comparison flipped so the result runs from largest to smallest.

## Run it

    python insertion_sort.py

That sorts several sample arrays (including empty, single-element, duplicate,
already-sorted, and reverse-sorted cases) and checks each result.

## How the decreasing order works

Standard insertion sort shifts elements that are *greater* than the key to the
right, which leaves the array increasing. To get decreasing order, the inner
loop instead shifts elements that are *smaller* than the key, so the larger
values end up at the front.

## Reference

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022).
*Introduction to Algorithms* (4th ed.). MIT Press.
