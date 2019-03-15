'''
    I decided to use open addressing with linear probing
    to handle collisions. I increment by 7 if a collision occurs.
    I chose to use this hashmap iteration because, while creation time may be slower,
    searches for this hashmap were not only more accurate but were much faster.
    Seeing as this is a 'search engine' I believe it is in the best interest of
    the users to use this type of hashmap.
'''


class HashMap:

    def __init__(self, input_file=None, url_stack=None, capacity=1000):
        '''
            initialize the HashMap object
            :param input_file: information to add to hash table
            :param capacity: size of hash table, default is 1,000
        '''
        self.input_file = input_file
        self.capacity = capacity
        self.size = 0
        self.map = [None] * self.capacity
        self.url_stack = url_stack

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
        '''
            Put the previous map into a temporary map,
            erase and increase the size of the map
            read through the temp map and move the keywords to the
            new map.
        :return:
        '''
        temp_map = self.map
        self.map = self.increase_capacity()
        for url_list in temp_map:
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
            hash_value = self.hash(key.lower())
            self.add(key.lower(), url, hash_value)

    def add(self, keyword, url, hash_value):
        '''
            First we check that the size of the map isn't too large
        :param keyword: keyword related to url
        :param url: url related to keyword
        :param hash_value: index value
        :return:
        '''
        if self.size >= self.capacity * (3 / 4):
            self.rehash_previous_list()

        if self.map[hash_value]:
            if self.map[hash_value][0] == keyword.lower():
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

    def search(self, operand_one=None, operand_two=None, operator=None):
        '''
            First, we check if all the operands and operators are there
            if they are,
                we add that string to the url_stack
                based on the operator, we send the search words to the
                corresponding function
            if they aren't
                we let the user know
        :param operand_one: first operand
        :param operand_two: second operand
        :param operator: AND/OR operator
        :return:
        '''
        if operand_one and operand_two and operator:
            self.url_stack.push(operand_one + ', ' + operand_two + ', ' + operator)
            if operator == '||':
                self.or_operator(operand_one.lower(), operand_two.lower())
            elif operator == '&&':
                self.and_operator(operand_one.lower(), operand_two.lower())
        else:
            print('You need both operands and an operator to perform search function.')

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
            for url in self.map[op_one_hashed][1:]:
                self.url_stack.push(url)
        else:
            print('Operand ', op_one, ' does not exist.')

        if op_two_hashed:
            for url in self.map[op_two_hashed][1:]:
                self.url_stack.push(url)
        else:
            print('Operand ', op_two, ' does not exist.')

    def and_operator(self, op_one, op_two):
        '''
            First we assign our hash values,
            if BOTH of those values exist,
                we first search for all the urls related to the first operand and
                add those to a temporary list
                Then, we search for all the urls related to the second operand,
                if those urls are in the temporary list we add that url to the url stack
            otherwise we let the user know that at least one of the operands doesn't exist
        :param op_one: first operand
        :param op_two: second operand
        :return:
        '''
        temp_list = []
        op_one_hashed = self.does_exist(op_one)
        op_two_hashed = self.does_exist(op_two)
        if op_one_hashed and op_two_hashed:
            for url in self.map[op_one_hashed][1:]:
                temp_list.append(url)
            for url in self.map[op_two_hashed][1:]:
                if url in temp_list:
                    self.url_stack.push(url)
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
        while self.map[operator_hashed] and self.map[operator_hashed][0] != operand:
            if operator_hashed + 7 < self.capacity:
                operator_hashed = operator_hashed + 7
            else:
                operator_hashed = (operator_hashed + 7) % self.capacity
        if self.map[operator_hashed]:
            return operator_hashed
        else:
            return None

    def increase_capacity(self):
        '''
            Doubles the size of the hash map
            Sets size back to 0
        :return: new list
        '''
        self.capacity = self.capacity * 2
        self.size = 0
        new_list = [None] * self.capacity
        return new_list