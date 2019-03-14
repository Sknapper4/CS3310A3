

class Stack:

    def __init__(self):
        self.items = []

    def __str__(self):
        to_string = ''
        for item in self.items:
            to_string += str(item) + ', '
        return to_string

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
