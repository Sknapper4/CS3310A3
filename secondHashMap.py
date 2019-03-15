# Use extends to add a list to the existing list


class HashMap:

    def __init__(self, input_file=None, capacity=1000):
        '''
            initialize the HashMap object
            :param input_file: information to add to hash table
            :param size: size of hash table, default is 1,000
        '''
        self.input_file = input_file
        self.capacity = capacity
        self.size = 0
        self.map = [None] * self.capacity

    def __str__(self):
        for url_list in self.map:
            for url in url_list:
                return ''

    def read_file(self):
        '''
            read the objects input file
            errors occur due to non UTF-8 ASCII chars, we will ignore them
            if a line is a url, assign it to the url variable
            if a line is keywords, assign it to the keywords list
            link that url to those keywords
        '''
        with open(self.input_file, errors='ignore') as f:
            for row in f:
                if row.startswith('http'):
                    url = row
                else:
                    keywords = row.split(' ')
                    self.link_url_to_keywords(url, keywords)
        print('Index Created \n')

    def hash(self, value):
        '''
            Take in the value to be hashed,
            if the value is a string, loop through the string,
            multiply the ascii value of each character by itself
            multiply the value by a large prime number
            return the total modded by the size of the map
            if the value is a number,
            square the number, multiply it by a large prime number
            return the total modded by the size of the map
            :param value: the value to be hashed
            :return: hash_value modded by map size
        '''
        hash_value = 0
        if isinstance(value, str):
            for char in list(value):
                hash_value += ord(char) * ord(char)
            return hash_value * 7717 % self.capacity
        else:
            hash_value = value * value
            return hash_value * 7717 % self.capacity

    def rehash_previous_list(self):

        for url_list in self.map:
            if url_list:
                keyword = url_list[0]
                for url in url_list[1:]:
                    self.add(keyword, url, self.hash(keyword))

    def link_url_to_keywords(self, url, keywords):
        '''
            Loop through each keyword in the keywords list
            find the hash value of each keyword
            add the keyword and the url to the map
        :param url: url connected to list of keywords
        :param keywords: list of keywords connected to url
        '''
        for key in keywords:
            hash_value = self.hash(key)
            self.add(key, url, hash_value)

    def add(self, keyword, url, hash_value):
        if self.size == self.capacity / 2:
            self.increase_capacity()
            self.rehash_previous_list()

        if self.map[hash_value]:
            if self.map[hash_value][0] == keyword:
                self.map[hash_value].append(url)
            else:
                if hash_value + 7 < self.capacity:
                    new_hash_value = hash_value + 7
                else:
                    new_hash_value = (hash_value + 7) % self.capacity
                self.add(keyword, url, new_hash_value)
        else:
            url_list = [keyword, url]
            self.map[hash_value] = url_list
            self.size += 1
        return

    def search(self, operand_one=None, operand_two=None, operator=None):
        if operand_one and operand_two and operator:
            if operator == '||':
                self.or_operator(operand_one, operand_two)
            elif operator == '&&':
                self.and_operator(operand_one, operand_two)

    def or_operator(self, op_one, op_two):
        '''
            First we assign our hash values, if those values aren't empty
            we go through the list of urls and add them to the stack
        :param op_one: first operator
        :param op_two: second operator
        '''
        op_one_hashed = self.does_exist(op_one)
        op_two_hashed = self.does_exist(op_two)
        if op_one_hashed:
            for index, url in enumerate(self.map[op_one_hashed][1:]):
                h = url
            print(index)
        else:
            print('Operand ', op_one, ' does not exist.')

        if op_two_hashed:
            for index, url in enumerate(self.map[op_two_hashed][1:]):
                h = url
            print(index)
        else:
            print('Operand ', op_two, ' does not exist.')

    def and_operator(self, op_one, op_two):
        op_one_hashed = self.does_exist(op_one)
        op_two_hashed = self.does_exist(op_two)
        if op_one_hashed and op_two_hashed:
            for index, url in enumerate(self.map[op_one_hashed][1:]):
                h = url
            print(index)
            for index, url in enumerate(self.map[op_two_hashed][1:]):
                h = url
            print(index)
        else:
            print('Both operands must exist to search using the AND operator.')

    def does_exist(self, operand):
        '''
            find the hash value of the operand,
            if it doesn't match our operand probe the map
            until you find the word or the index is empty
        :param operand: the keyword to be found
        :return: none if the index is empty,
                the index value if the operand is found
        '''
        operator_hashed = self.hash(operand)
        while self.map[operator_hashed][0] and self.map[operator_hashed][0] != operand:
            if operator_hashed + 7 < self.capacity:
                operator_hashed = operator_hashed + 7
            else:
                operator_hashed = (operator_hashed + 7) % self.capacity
            if not self.map[operator_hashed]:
                return None
        return operator_hashed

    def increase_capacity(self):
        '''
            Doubles the size of the hash map
        :return:
        '''
        new_list = [None] * self.capacity
        self.map.extend(new_list)
        self.capacity = self.capacity * 2
