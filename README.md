# Search Algorithms <!-- omit in toc -->

## Table of contents <!-- omit in toc -->

Collection of algorithms that are commonly used in computer science to search for elements within a defined search space.

- [Binary-Search, Half-Interval-Search, Logarithmic-Search](#binary-search-half-interval-search-logarithmic-search)
- [Interpolation-Search, Interval-Search](#interpolation-search-interval-search)

## Binary-Search, Half-Interval-Search, Logarithmic-Search

Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found.

| Case     | Time complexity |
|----------|-----------------|
| Worst       | O(log n)     |
| Best        | O(1)         |
| Average     | O(log n)     |

Run [binary_search.py](src/binary_search.py)

The script will execute several test methods with a random generated dataset and an random selected search element for which the algorithm is used to find the index.

Formular for calculating the slicing element

l&r = left and right border

$$ p = (l+r)/2 $$

## Interpolation-Search, Interval-Search

| Case     | Time complexity  |
|----------|------------------|
| Worst       | O(n)          |
| Best        | O(1)          |
| Average     | O(log(log(n)) |

The idea behind this algorithm is compareable to how people would search in a phone book or any other alphabetical ordered list. With the use of a linear interpolation the algorithm tries to calculate where in the remaining search space for the sought item might be.

Run [interpolation_search.py](src/interpolation_search.py)

Formular for calculating the slicing element

E = List of elements,
v = Search element,
l&r = left and right border

$$ p = l + {v - E[l] \over E[r]-E[l]} * (r-l) $$
