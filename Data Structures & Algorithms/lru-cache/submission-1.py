from collections import defaultdict

class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key, self.val = key, val
        self.prev, self.next = prev, next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = defaultdict(Node)    
        self.left, self.right = Node(), Node()
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        last_node = self.right.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        node.next.prev, node.prev.next = node.prev , node.next

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.capacity:
            node = self.left.next 
            self.remove(node)
            del self.cache[node.key]
    
