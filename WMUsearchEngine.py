from secondHashMap import HashMap
from stack import Stack

import time


def wmu_search_engine(input_file):
    first_hashmap = HashMap(input_file)
    return first_hashmap


def read_instructions(instruction_file):
    instruction_stack = Stack()
    with open(instruction_file) as f:
        for row in f:
            instruction_stack.push(row.strip())
    return instruction_stack


if __name__ == '__main__':
    in_file = 'inputs/url.txt'
    instructions = 'inputs/test.txt'

    h = HashMap(in_file)
    h.read_file()
    print(h)
    # create_start_time = time.time()

    # hashmap = wmu_search_engine(in_file)
    #
    # creation_total_time = time.time() - create_start_time
    #
    # # print(hashmap)
    # search_start = time.time()
    #
    # hashmap.search('older', 'people', '||')
    # search_end = time.time() - search_start
    # print('Creation time: ', creation_total_time, ' seconds')
    # print('Search time for "or" operator: ', search_end, ' seconds.')
