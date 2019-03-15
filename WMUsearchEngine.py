from bestHashMap import HashMap
from stack import Stack
from headers import INPUT_FILE, INSTRUCTION_FILE

import time


def wmu_search_engine():
    hashmap.read_file()
    hashmap.search('older', 'nothingthsda', '||')
    print(url_stack.size())
    while instruction_stack.size() > 0:
        print(instruction_stack.pop())


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


if __name__ == '__main__':
    url_stack = Stack()
    instruction_stack = read_instructions()

    hashmap = HashMap(INPUT_FILE, url_stack)
    wmu_search_engine()
