from secondHashMap import HashMap
from stack import Stack
from headers import INPUT_FILE, INSTRUCTION_FILE

import time


def wmu_search_engine():
    hashmap = HashMap(INPUT_FILE)
    return hashmap


def read_instructions():
    single_words_stack = Stack()
    instruction_stack = Stack()
    with open(INSTRUCTION_FILE) as f:
        for row in f:
            single_words_stack.push(row.strip())
    return instruction_stack


if __name__ == '__main__':
    url_stack = Stack()
    create_start_time = time.time()
    h = HashMap(INPUT_FILE)
    h.read_file()
    creation_total_time = time.time() - create_start_time
    h.search('yellow', 'older', '&&')

    print('Creation time: ', creation_total_time, ' seconds')
