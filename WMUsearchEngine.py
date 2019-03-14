from hashmapIterations.firstHashMap import HashMap

import time


def wmu_search_engine(input_file):
    first_hashmap = HashMap(input_file)
    return first_hashmap


if __name__ == '__main__':
    in_file = 'inputs/url.txt'

    create_start_time = time.time()

    hashmap = wmu_search_engine(in_file)

    creation_total_time = time.time() - create_start_time

    # print(hashmap)
    search_start = time.time()

    hashmap.search('older', 'people', '||')
    search_end = time.time() - search_start
    print('Creation time: ', creation_total_time, ' seconds')
    print('Search time for "or" operator: ', search_end, ' seconds.')
