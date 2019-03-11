from secondHashMap import HashMap


def wmu_search_engine(input_file):
    num_lines = sum(1 for line in open(input_file, errors='ignore'))
    print(num_lines)
    first_hashmap = HashMap(num_lines, input_file)
    return first_hashmap


if __name__ == '__main__':
    hashmap = wmu_search_engine('inputs/test.txt')
    # print(hashmap)
    hashmap.search('older', 'people', '||')
