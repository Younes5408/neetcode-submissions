class Node:
    def __init__(self, key,val ):
        self.next=self.prv= None
        self.val ,self.key= val,key

    
class LRUCache:

    def __init__(self, cap: int):
        self.cache = {}
        self.cap = cap
        
        self.l = self.r = Node(0,0)
        self.l.next ,self.r.prv = self.r , self.l


    def remove(self,node:Node):
        pr , nxt = node.prv , node.next
        pr.next , nxt.prv = nxt ,pr 
        
    def insert(self, node: Node):
        pr , n =  self.r.prv , self.r
        pr.next, n.prv = node, node

        node.next ,node.prv = n,pr
 
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
      
    def put(self, key: int, value: int) -> None:
        if key in self.cache :
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru= self.l.next
            self.remove(lru)
            del self.cache[lru.key]


        