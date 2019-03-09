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

    def add_new_object(self, value):
        if not self.hash_map:
            self.create_hash_map()
        keyword = value[0]
        url = value[1]
        index_place = self.hash_value(keyword)
        if len(self.hash_map[index_place]) > 0:
            index = 0
            for x in self.hash_map[index_place]:
                index += 1
                if x[0] == keyword:
                    # print(x[0])
                    self.hash_map[index_place][index - 1].append(url)
                    return
                elif x is None:
                    self.hash_map[index_place][index - 1] = value
                    return
        self.hash_map[index_place].append(value)

    def hash_value(self, value):
        # TODO hash the value
        index = len(value) * 6 % self.map_size
        return index

    def delete_object(self, value):
        value_to_be_hashed = value[0]
        index_place = self.hash_value(value_to_be_hashed)
        if len(self.hash_map[index_place]) > 1:
            index = 0
            for x in self.hash_map[index_place]:
                index += 1
                if x[0] is value_to_be_hashed:
                    self.hash_map[index_place][index - 1] = None
                    return
        else:
            self.hash_map[index_place] = []

    def find_urls_with_keywords(self, operand_one=None, operand_two=None, operator=None):
        urls = []
        if operand_one and operand_two and operator:
            if operator == '||':
                print('or')
                index_place = self.hash_value(operand_one)
                for x in self.hash_map[index_place]:
                    if x[0] == operand_one:
                        for url in x:
                            if url.startswith('http'):
                                urls.append(url)
                index_place = self.hash_value(operand_two)
                for x in self.hash_map[index_place]:
                    if x[0] == operand_one:
                        for url in x:
                            if url.startswith('http'):
                                if url not in urls:
                                    urls.append(url)
                print(urls)
                return
            if operator == '&&':
                print('and')
                return
