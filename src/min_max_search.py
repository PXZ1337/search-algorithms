from test_utils import test_min_max_search

def min(elements: list) -> int:
    min = elements[0]
    for _, v in enumerate(elements[1:]):
        if (v < min):
            min = v 
    
    return min

def max(elements: list) -> int:
    max = elements[0]
    for _, v in enumerate(elements[1:]):
        if (v > max):
            max = v 
    
    return max

def min_max_tournament_search(elements: list) -> list:
    winner, loser = [], []
    for _, i in enumerate(range(0, len(elements), 2)):
        if elements[i] > elements[i+1]:
            winner.append(elements[i])
            loser.append(elements[i+1])
        else:
            loser.append(elements[i])
            winner.append(elements[i+1])
    
    result: list = []
    result.append(min(loser))
    result.append(max(winner))

    return result
    

if __name__ == '__main__':
    test_min_max_search(size_of_sample_set=2**6, min_max_search_func=min_max_tournament_search)
    test_min_max_search(size_of_sample_set=2**7, min_max_search_func=min_max_tournament_search)
    test_min_max_search(size_of_sample_set=2**8, min_max_search_func=min_max_tournament_search)