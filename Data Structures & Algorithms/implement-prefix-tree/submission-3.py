class Node:
    def __init__(self):
        self.children = {}
        self.is_end= False

class PrefixTree:

    def __init__(self):
        self.node= Node()
        
    def insert(self, word: str) -> None:
        curr = self.node

        for c in word :
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.node

        for c in word :
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.node

        for c in prefix :
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
