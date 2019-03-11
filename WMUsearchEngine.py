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
                first_hashmap.link_url_to_keyword(url, keywords)
    print('Index Created\n')
    return first_hashmap


if __name__ == '__main__':
    hashmap = read_input_file('inputs/url.txt')
    hashmap.search('older', 'people', '&&')
