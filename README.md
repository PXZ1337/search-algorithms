# Search Algorithms

Collection of algorithms that are commonly used in computer science to search for elements within a defined search space.

## Binary / Half-Interval / Logarithmic-Search

Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. 

| Case     | Time complexity |
|----------|-----------------|
| Worst       | O(log n)     |
| Best        | O(1)         |
| Average     | O(log n)     |

Run [binary_search.py](src/binary_search.py)

The script will execute several test methods with a random generated dataset and an random selected search element for which the algorithm is used to find the index.

