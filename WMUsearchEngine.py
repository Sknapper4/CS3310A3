from firstHashMap import HashMap
import sys


def read_input_file(input_file):
    num_lines = sum(1 for line in open(input_file))
    first_hashmap = HashMap(num_lines)
    with open('inputs/urls.txt') as f:
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
    return first_hashmap


def link_url_to_keyword(url, keywords, hashmap):
    for x in keywords:
        linked_items = [x, url]
        hashmap.add_new_object(linked_items)
    # print(hashmap)


def search():
    # TODO allow user to look for urls with keywords
    print('searching')
    first_hashmap.find_urls_with_keywords('red', 'fast', '||')
    return


def delete():
    # TODO allow user to delete urls with keywords
    return


first_hashmap = read_input_file('inputs/urls.txt')
search()
