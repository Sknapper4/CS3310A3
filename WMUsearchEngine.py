from firstHashMap import HashMap
import sys


def read_input_file(input_file):
    num_lines = sum(1 for line in open(input_file, errors='ignore'))
    print(num_lines)
    first_hashmap = HashMap(num_lines)
    with open(input_file, errors='ignore') as f:
        for row in f:
            have_both_items = False
            line = row.split(' ')
            if line[0].startswith('http'):
                url = line[0]
            else:
                keywords = line
                have_both_items = True
            if have_both_items:
                link_url_to_keyword(url, keywords, first_hashmap)
    print('Index Created\n')
    return first_hashmap


def link_url_to_keyword(url, keywords, hashmap):
    for x in keywords:
        linked_items = [x, url]
        hashmap.add_new_object(linked_items)
    # print(hashmap)


def search(operand_one, operand_two, operator):
    # TODO allow user to look for urls with keywords
    print('searching')
    hashmap.find_urls_with_keywords(operand_one, operand_two, operator)
    return


def delete():
    # TODO allow user to delete urls with keywords
    return


hashmap = read_input_file('inputs/url.txt')
search('older', 'people', '&&')
