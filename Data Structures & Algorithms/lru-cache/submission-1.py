class Node:
    def __init__(self, key,value):
        self.key , self.val= key,value
        self.next = self.prev= None
class LRUCache:

    def __init__(self, cap: int):
        self.cache = {}
        self.cap=cap

        self.left = self.right = Node(0,0)
        self.left.next, self.right.prev =self.right, self.left
        
    def remove(self,node:Node):
        prv, nxt = node.prev , node.next
        prv.next , nxt.prev = node.next, node.prev


    def insert(self, node: Node):
        prv, nxt = self.right.prev ,self.right
        prv.next , nxt.prev = node , node
        node.next , node.prev = self.right , prv
    def get(self, key: int) -> int:
        if  key not in self.cache:
            return -1
        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val  

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert( self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru) #remove from linked list
            del self.cache[lru.key]