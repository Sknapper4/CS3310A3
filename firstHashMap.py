import random


class HashMap:

    def __init__(self, num_elements, hash_map=None):
        self.map_size = num_elements * 5
        self.hash_map = hash_map

    def __str__(self):
        print(self.map_size)
        return str(self.hash_map)

    def create_hash_map(self):
        self.hash_map = [[] for x in range(self.map_size)]

    def link_url_to_keyword(self, url, keywords):
        for key in keywords:
            self.add_new_object(key, url)

    def search(self, operand_one, operand_two, operator):
        print('searching')
        self.find_urls_with_keywords(operand_one, operand_two, operator)
        return

    def add_new_object(self, keyword, url):
        if not self.hash_map:
            self.create_hash_map()
        index_place = self.hash_value(keyword)
        if len(self.hash_map[index_place]) > 0:
            for x in self.hash_map[index_place]:
                if x[0] == keyword:
                    # print(x[0])
                    self.hash_map[index_place][x.index - 1].append(url)
                    return
                elif x is None:
                    self.hash_map[index_place][x.index - 1] = [keyword, url]
                    return
        self.hash_map[index_place].append([keyword, url])

    def hash_value(self, value):
        return len(value) * 6 % self.map_size

    def delete_object(self, value):
        value_to_be_hashed = value[0]
        index_place = self.hash_value(value_to_be_hashed)
        if len(self.hash_map[index_place]) > 1:
            for x in self.hash_map[index_place]:
                if x[0] is value_to_be_hashed:
                    self.hash_map[index_place][x.index - 1] = None
                    return
        else:
            self.hash_map[index_place] = []

    def find_urls_with_keywords(self, operand_one=None, operand_two=None, operator=None):
        if operand_one and operand_two and operator:
            if operator == '||':
                self.or_operator(operand_one, operand_two)
                return
            if operator == '&&':
                self.and_operator(operand_one, operand_two)
                return
        else:
            print('You don\'t have enough keywords')

    def or_operator(self, operand_one, operand_two):
        urls = []
        print('or')
        index_place = self.hash_value(operand_one)
        print(index_place)
        for x in self.hash_map[index_place]:
            if x[0].lower() == operand_one.lower():
                for url in x:
                    if url.startswith('http'):
                        urls.append(url)
        index_place = self.hash_value(operand_two)
        for x in self.hash_map[index_place]:
            if x[0].lower() == operand_one.lower():
                for url in x:
                    if url.startswith('http') and url not in urls:
                        urls.append(url)
        for url in urls:
            print(url)
        print(len(urls))

    def and_operator(self, operand_one, operand_two):
        print('and')
        urls = []
        first_keyword = []
        index_place = self.hash_value(operand_one)
        for x in self.hash_map[index_place]:
            if x[0].lower() == operand_one.lower():
                for url in x:
                    if url.startswith('http') and url not in first_keyword:
                        first_keyword.append(url)
        index_place = self.hash_value(operand_two)
        for x in self.hash_map[index_place]:
            if x[0].lower() == operand_two.lower():
                for url in x:
                    if url.startswith('http') and url in first_keyword and url not in urls:
                        urls.append(url)
        for url in urls:
            print(url)
        print(len(urls))
