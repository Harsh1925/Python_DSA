class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def insert_node_after(prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            return

        else:
            while key != cur_node.data:
                prev_node = cur_node
                cur_node = cur_node.next

            prev_node.next = cur_node.next

    def delete_node_at_pos(self, pos):
        cur_node = self.head
        cur_pos = 0
        if pos == cur_pos:
            self.head = cur_node.next
            return
        else:
            while cur_node and cur_pos != pos:
                prev_node = cur_node
                cur_node = cur_node.next
                cur_pos += 1

            if cur_node is None:
                return

            prev_node.next = cur_node.next

    def get_node_details(self, node_value):
        cur_node = self.head
        prev_node = None
        while cur_node.data != node_value:
            prev_node = cur_node
            cur_node = cur_node.next
        return prev_node, cur_node

    def swap_node(self, node_1, node_2):
        node1_prev, node1_cur = self.get_node_details(node_1)
        node2_prev, node2_cur = self.get_node_details(node_2)

        if node1_prev:
            node1_prev.next = node2_cur
        if node2_prev:
            node2_prev.next = node1_cur

        if node2_prev is None:
            self.head = node1_cur
        elif node1_prev is None:
            self.head = node2_cur

        node2_next = node2_cur.next
        node1_next = node1_cur.next

        node2_cur.next = node1_next
        node1_cur.next = node2_next

    def rev_node_list(self):
        cur_node = self.head
        prev_node = None
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node

    def rev_node_group(self, head, num):
        if head is None:
            return
        cur_node = head
        next_node = None
        prev_node = None
        i = 0
        while cur_node and i < num:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
            i += 1

        if next_node is not None:
            head.next = self.rev_node_group(next_node, num)

        return prev_node

    def rotate_list(self, num):
        cur = self.head
        count = 1
        while cur:
            if count == num:
                temp = cur
                prev.next = None
            prev = cur
            cur = cur.next
            count += 1

        prev.next = self.head
        self.head = temp

    def remove_duplicate(self):
        cur = self.head
        prev = None
        while cur:
            cur_2 = cur.next
            while cur_2:
                if cur_2 is None:
                    break
                if cur_2.data == cur.data:
                    prev.next = cur_2.next
                    cur_2 = cur_2.next
                else:
                    prev = cur_2
                    cur_2 = cur_2.next

            cur = cur.next

    def is_pelindrome(self):
        s = ""
        cur = self.head
        while cur:
            s += cur.data
            cur = cur.next

        return s == s[::-1]


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("B")
llist.append("A")
"""
print(llist.is_pelindrome())
llist.rotate_list(5)
llist.remove_duplicate()
llist.head = llist.rev_node_group(llist.head, 3)
llist.swap_node("A", "B")
llist.prepend("E")
llist.insert_node_after(llist.head.next, "X")
llist.print_list()
print("======================")
llist.delete_node("B")
llist.print_list()
print("======================")
llist.delete_node_at_pos(3)"""
llist.print_list()
