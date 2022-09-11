#TC - O(n), where NN is the length of the sentence
#SC - O(n)
class TrieNode: 
    
    def __init__(self):
        
        self.isEnd = False
        self.childrens = [None]*26
        
class Trie(object):
    
    def __init__(self):
        self.root = TrieNode()
    
    def getroot(self):
        return self.root
        
    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            key = ord(char) - ord('a')
            if curr.childrens[key] == None:
                curr.childrens[key] = TrieNode()
            
            curr = curr.childrens[key]
        curr.isEnd = True
        
class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie()
        for prefixwords in dictionary:
            trie.insert(prefixwords)
            
        resultstr = []
        sentence = sentence.split()
        for word in sentence:
            curr = trie.getroot()
            currword = ""
            for char in word:
                key = ord(char) - ord('a')
                if curr.childrens[key] == None or curr.isEnd == True:
                    break
                currword += char
                curr = curr.childrens[key]
            
            if curr.isEnd == True:
                resultstr.append(currword)
            
            else:
                resultstr.append(word)
        
        return " ".join(resultstr)