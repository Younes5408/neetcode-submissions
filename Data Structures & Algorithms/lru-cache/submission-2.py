class Node:
    def __init__(self, key , value):
        self.next = self.prev = None
        self.key , self.value = key, value
class LRUCache:
    def __init__(self, cap: int):
        self.cache = {}
        self.cap = cap
        self.right = self.left = Node(0,0)

        self.left.next, self.right.prev = self.right ,self.left
       
    def remove(self,node:Node):
        pr , nxt = node.prev , node.next
        pr.next, nxt.prev = nxt , pr
 
    def insert(self, node: Node):
        pr ,nxt = self.right.prev ,self.right
        pr.next, nxt.prev =  node, node

        node.next, node.prev = self.right ,pr

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
     
    def put(self, key: int, value: int) -> None:
        if key  in self.cache:
            self.remove(self.cache[key])
        self.cache[key]= Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache)>self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
    