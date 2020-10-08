# Making a Node class to specify a blueprint for the node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.node = {
            'value': self.value,
            'next': self.next,
            'prev': self.prev
        }

# defining LinkedList Class


class LinkedList(Node):
    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None,
            'prev': None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        '''
        adds a node to the end of the linkedlist
        '''
        newNode = Node(value)
        hold = self.tail
        self.tail['next'] = newNode.node
        self.tail = newNode.node
        self.tail['prev'] = hold
        self.length += 1

    def prepend(self, value):
        '''
        adds a node to the beginning of the Linkedlist
        '''
        newNode = Node(value)
        self.head['prev'] = newNode.node
        newNode.node['next'] = self.head
        self.head = newNode.node
        self.length += 1

    def insert(self, index, value):
        '''
        Inserts a node at a specific position in the list
        '''
        if index >= self.length:
            return self.append(value)
        elif index == 0:
            return self.prepend(value)
        else:
            newNode = Node(value)
            i = 0
            current_node = self.head
            while i != index-1:
                current_node = current_node['next']
                i += 1
            follower = current_node['next']
            current_node['next'] = newNode.node
            newNode.node['next'] = follower
            follower['prev'] = newNode.node
            newNode.node['prev'] = current_node
            self.length += 1

    def show_list(self):
        '''
        prints the list
        '''
        elements = []
        current_node = self.head
        while current_node != None:
            elements.append(current_node['value'])
            current_node = current_node['next']
        return elements

    def reverse(self):
        '''
        reverses the list
        '''
        elements_rev = []
        current_node = self.tail
        while current_node != None:
            elements_rev.append(current_node['value'])
            current_node = current_node['prev']
            # print(current_node['prev'])
        return elements_rev


ll = LinkedList(10)
ll.append(23)
ll.append(24)
ll.prepend(221)
ll.insert(2, 212)
ll.insert(0, 1000)
print(ll.tail['value'])
print(ll.head['prev'])
print(ll.length)
print(ll.show_list())
print(ll.reverse())
