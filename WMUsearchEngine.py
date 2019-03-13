from secondHashMap import HashMap


def wmu_search_engine(input_file):
    first_hashmap = HashMap(input_file)
    return first_hashmap


if __name__ == '__main__':
    in_file = 'inputs/url.txt'
    hashmap = wmu_search_engine(in_file)
    # print(hashmap)
    hashmap.search('older', 'people', '||')
