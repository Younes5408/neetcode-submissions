class TrieNode:
    def __init__(self):
        self.children= {}
        self.is_end = False
class WordDictionary:
    def __init__(self):
        self.root= TrieNode()
    def addWord(self, word: str) -> None:
        curr= self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr= curr.children[c]
        curr.is_end = True
        
    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root

            for x in range(i, len(word)):
                c=word[x]
                if c == ".":
                    for ch in curr.children.values():
                        if dfs(x+1,ch):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.is_end
        return dfs(0,self.root)        