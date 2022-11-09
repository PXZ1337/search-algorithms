import random, time

def interpolation_search(val: int, elements: list) -> int:
    l, r = 0, len(elements)-1
    while (val >= elements[l] and val <= elements[r]):
        p = round(l + ((val-elements[l]) / (elements[r]-elements[l])) * (r-l))
        if (val > elements[p]):
            l = p+1
        elif (val < elements[p]):
            r = p-1
        else:
            return p

    return -1
    
def test_interpolation_search(size_of_sample_set: int):
    x, y = -size_of_sample_set, size_of_sample_set
    sample_list = random.sample(range(x, y), size_of_sample_set)
    sample_list.sort()
    search_elem = random.choice(sample_list)
    
    start_time = time.time()
    i = interpolation_search(*(search_elem, sample_list))
    print("took %s" % (time.time() - start_time))

    assert search_elem == sample_list[i]

    print(f"Found {sample_list[i]} on index {i} in list: {sample_list[:10]}.. (searched for: {search_elem})")

def test_interpolation_search_not_found():
    sample_list = random.sample(range(0, 100), 15)
    sample_list.sort()
    search_elem = 120

    assert interpolation_search(*(search_elem, sample_list)) == -1

    print(f"Did not found {search_elem} in list: {sample_list[:10]}..")


if __name__ == "__main__":
    test_interpolation_search_not_found()
    test_interpolation_search(10000)
    test_interpolation_search(100000) 
    test_interpolation_search(1000000) 
 