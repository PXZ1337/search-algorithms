from test_utils import test_search_func, test_search_func_not_found

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
    

if __name__ == "__main__":
    test_search_func_not_found(search_func=interpolation_search)
    test_search_func(size_of_sample_set=1000, search_func=interpolation_search)
    test_search_func(size_of_sample_set=10000, search_func=interpolation_search)
    test_search_func(size_of_sample_set=100000, search_func=interpolation_search)
    test_search_func(size_of_sample_set=1000000, search_func=interpolation_search)
