from secondHashMap import HashMap
from stack import Stack
from headers import INPUT_FILE, INSTRUCTION_FILE

import time


def wmu_search_engine():
    hashmap = HashMap(INPUT_FILE)
    return hashmap


def read_instructions():
    '''
        Open the file, add every word to the word stack
        if we encounter an operator, add the last two words and the operator to a string
        add that string to the instruction stack
        if we encounter a ? or ! add that to the instruction stack by itself
    :return: the instructions
    '''
    word_stack = Stack()
    instruction_stack = Stack()
    with open(INSTRUCTION_FILE) as f:
        for row in f:
            if row.strip() == '&&' or row.strip() == '||':
                if word_stack.size() >= 2:
                    instruction_string = str(word_stack.pop())
                    instruction_string += ' ' + str(word_stack.pop())
                    instruction_string += ' ' + str(row.strip())
                    instruction_stack.push(instruction_string)
            elif row.strip() == '?' or row.strip() == '!':
                instruction_stack.push(row.strip())
            else:
                word_stack.push(row.strip())
    return instruction_stack


if __name__ == '__main__':
    url_stack = Stack()
    s = read_instructions()

    create_start_time = time.time()

    h = HashMap(INPUT_FILE, url_stack)
    h.read_file()

    creation_total_time = time.time() - create_start_time

    start = time.time()
    h.search('information', 'Older', '||')
    print('search time ', (time.time() - start))

    print('Creation time: ', creation_total_time, ' seconds')
