class HashMap:

    def __init__(self, input_file=None):
        self.input_file = input_file

    def read_file(self):
        # TODO read input file for URLs
        return

    def hash(self, value):
        # TODO create a hash algorithm, return that value
        hash_value = 0
        for char in list(value):
            hash_value += ord(char) * ord(char)
        return hash_value

    def link_url_to_keywords(self, url, keywords):
        # TODO separate keywords, add each keyword with the URL
        return

    def add(self, keyword, url, hash_value):
        # TODO add new object to the hash table
        return

    def search(self, operand_one=None, operand_two=None, operator=None):
        # TODO use operands and operators to search for values in the hash table
        return
