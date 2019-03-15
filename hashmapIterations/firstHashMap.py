# Stephen Knapper
# stephen.a.knapper@wmich.edu
'''
In this first implementation of my hash table,
I first create an empty hash table directly correlated to
the size of the file. I then read the file in and connect
each url to its set of keywords.
To resolve collisions, I used separate chaining.
'''


class HashMap:

    def __init__(self, input_file=None):
        self.map_size = (sum(1 for line in open(input_file, errors='ignore'))) * 2
        self.hash_map = [[] for x in range(self.map_size)]
        self.input_file = input_file
        self.read_file()

    def __str__(self):
        print(self.map_size)
        return str(self.hash_map)

    def read_file(self):
        with open(self.input_file, errors='ignore') as f:
            for row in f:
                line = row.split(' ')
                if line[0].startswith('http'):
                    url = line[0]
                else:
                    keywords = line
                    self.link_url_to_keyword(url, keywords)
        print('Index Created\n')

    def link_url_to_keyword(self, url, keywords):
        # print('linking')
        for key in keywords:
            self.add_new_object(key, url)

    def add_new_object(self, keyword, url):
        # print('adding')
        if not self.hash_map:
            self.read_file()
        index_place = self.hash_value(keyword)
        if self.hash_map[index_place]:
            for index, x in enumerate(self.hash_map[index_place]):
                if x[0] == keyword:
                    # print('here')
                    self.hash_map[index_place][index].append(url)
                    return
                elif x is None:
                    self.hash_map[index_place][index] = [keyword, url]
                    return
        self.hash_map[index_place].append([keyword, url])

    def hash_value(self, value):
        return len(value) * 6 % self.map_size

    def search(self, operand_one=None, operand_two=None, operator=None):
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
        index_place = self.hash_value(operand_one)
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
