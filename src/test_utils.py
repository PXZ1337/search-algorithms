import random, time
from typing import Callable

def test_search_func(size_of_sample_set: int, search_func: Callable):
    x, y = -size_of_sample_set, size_of_sample_set
    sample_list = random.sample(range(x, y), size_of_sample_set)
    sample_list.sort()
    search_elem = random.choice(sample_list)
    
    start_time = time.time()
    i = search_func(*(search_elem, sample_list))
    print("took %s" % (time.time() - start_time))

    assert search_elem == sample_list[i]

    print(f"Found {sample_list[i]} on index {i} in list: {sample_list[:10]}.. (searched for: {search_elem})")

def test_search_func_not_found(search_func: Callable):
    sample_list = random.sample(range(0, 100), 15)
    sample_list.sort()
    search_elem = 120

    start_time = time.time()
    assert search_func(*(search_elem, sample_list)) == -1
    print("took %s" % (time.time() - start_time))
    print(f"Did not found {search_elem} in list: {sample_list[:10]}..")