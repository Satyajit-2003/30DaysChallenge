# This is a linked list question
# Maintain a doubly linked list and a hashmap
# The hashmap will store the key and the node
# Insert: Insert the node at the head
# Delete: Delete the node from the tail
# Get: If the key is present, delete the node and insert it at the head
# Put: If the key is present, update the value, delete the node and insert it at the head

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.size = 0
        # Initialize Double LL, 2 dummy nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        # Joining two nodes
        self.head.prev = self.tail
        self.head.next = None
        self.tail.prev = None
        self.tail.next = self.head
    
    def insert(self, node):
        # Modifying the links of node
        node.next = self.head
        node.prev = self.head.prev
        
        # Modifying the list
        self.head.prev = node
        node.prev.next = node

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev               

    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return
        if self.size == self.capacity:
            del self.cache[self.tail.next.key]
            self.delete(self.tail.next)
            self.size -= 1
        self.size += 1
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)