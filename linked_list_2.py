class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        cur = self.head
        while cur:
            prev = cur
            cur = cur.next

        prev.next = new_node

    def print_list(self):

        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def merge_sort_list(self):

        p_list = llist.head
        q_list = llist_2.head
        if p_list.data > q_list.data:
            self.head = q_list
            cur = q_list
            q_list = q_list.next
        else:
            self.head = p_list
            cur = p_list
            p_list = p_list.next

        while p_list and q_list:
            if p_list.data > q_list.data:
                cur.next = q_list
                q_list = q_list.next
                cur = cur.next
            else:
                cur.next = p_list
                p_list = p_list.next
                cur = cur.next

        while p_list or q_list:
            if q_list:
                cur.next = q_list
                q_list = q_list.next
                cur = cur.next
            else:
                cur.next = p_list
                p_list = p_list.next
                cur = cur.next


llist = LinkedList()
llist.append(1)
llist.append(4)
llist.append(5)
llist.append(7)
llist.append(9)
llist.append(10)
llist_2 = LinkedList()
llist_2.append(2)
llist_2.append(3)
llist_2.append(6)
llist_2.append(8)
llist.merge_sort_list()
llist.print_list()








