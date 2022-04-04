"""Stack datastructures"""


class Stack:
    def __init__(self):
        self.names = []

    def push(self, item):
        self.names.append(item)

    def pop(self):
        return self.names.pop()

    def is_empty(self):
        return self.names == []

    def peek(self):
        if not self.is_empty():
            return self.names[-1]

    def get_stack(self):
        return self.names


def reverse_string(stack, input_str):
    # print(input_str[::-1])
    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


s = Stack()
print(s.is_empty())
s.push("A")
s.push("B")
s.push("C")
print(s.get_stack())
s.pop()
print(s.get_stack())
print(s.is_empty())
print(s.peek())
stack = Stack()
print(reverse_string(stack, "Hello"))
