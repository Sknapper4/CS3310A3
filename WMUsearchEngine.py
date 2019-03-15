# Stephen Knapper
# stephen.a.knapper@wmich.edu
from bestHashMap import HashMap
from stack import Stack
from headers import INPUT_FILE, INSTRUCTION_FILE

import time
import sys


def wmu_search_engine():
    while instruction_stack.size() > 0:
        instruction = instruction_stack.pop()
        instruction = instruction.split(' ')
        if len(instruction) == 3:
            op_one = instruction[0].upper()
            op_two = instruction[1].upper()
            operator = instruction[2]
            start_time = time.time()
            hashmap.search(op_one, op_two, operator)
            end_time = time.time() - start_time
            search_time_string = f'Searching for "%s, %s, %s" took %.6f seconds.' % \
                                 (instruction[0], instruction[1], instruction[2], end_time)
            search_time_stack.push(search_time_string)
        elif instruction[0] == '!' or instruction[0] == '?':
            url_stack.push(instruction[0])


def read_instructions():
    '''
        Open the file, add every word to the word stack
        if we encounter an operator, add the last two words and the operator to a string
        add that string to the instruction stack
        if we encounter a ? or ! add that to the instruction stack by itself
    :return: the instructions
    '''
    word_stack = Stack()
    instructions = Stack()
    with open(INSTRUCTION_FILE) as f:
        for row in f:
            if row.strip() == '&&' or row.strip() == '||':
                if word_stack.size() >= 2:
                    instruction_string = str(word_stack.pop())
                    instruction_string += ' ' + str(word_stack.pop())
                    instruction_string += ' ' + str(row.strip())
                    instructions.push(instruction_string)
            elif row.strip() == '?' or row.strip() == '!':
                instructions.push(row.strip())
            else:
                word_stack.push(row.strip())
    return instructions


def write_urls_to_file(stack):
    output_file = open('output/url_stack.txt', 'w')

    while stack.peek() != '!':
        output_file.write(stack.pop() + '\n')
    output_file.write(stack.pop() + '\nEND OF FILE')
    output_file.close()


def write_results_to_file():
    results_file = open('output/results.txt', 'w')
    while not search_time_stack.is_empty():
        results_file.write(search_time_stack.pop() + '\n')
    results_file.close()


if __name__ == '__main__':
    url_stack = Stack()
    search_time_stack = Stack()
    instruction_stack = read_instructions()

    hashmap_creation_start = time.time()

    hashmap = HashMap(sys.argv[1], url_stack)
    hashmap.read_file()

    hashmap_creation_end = time.time() - hashmap_creation_start

    wmu_search_engine()

    url_stack.size()

    write_urls_to_file(url_stack)

    write_results_to_file()
