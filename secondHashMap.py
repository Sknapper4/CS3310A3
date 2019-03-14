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
        # TODO read input file for URLs
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

    def rehash(self, value):
        # TODO create a rehashing algorithm
        rehash_value = 0
        if isinstance(value, str):
            for char in list(value):
                rehash_value += ord(char) * 19
            return rehash_value * ord(list(value)[0]) % self.capacity
        else:
            rehash_value = value * 19
            return rehash_value * value % self.capacity

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
        # TODO add new object to the hash table
        if self.size == self.capacity/2:
            self.increase_capacity()

        if self.map[hash_value]:
            if self.map[hash_value][0] == keyword:
                self.map[hash_value].append(url)
            else:
                if hash_value + 7 < self.capacity:
                    new_hash_value = hash_value + 7
                else:
                    new_hash_value = hash_value / 2 + 7
                self.add(keyword, url, new_hash_value)
        else:
            url_list = [keyword, url]
            self.map[hash_value] = url_list
            self.size += 1
        return

    def search(self, operand_one=None, operand_two=None, operator=None):
        # TODO use operands and operators to search for values in the hash table
        return

    def increase_capacity(self):
        new_list = [None] * self.capacity
        self.map.extend(new_list)
        self.capacity = self.capacity * 2
