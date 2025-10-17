import unittest
from typing import List,Dict, Optional, Tuple

class Node:
    def __init__(self, childs=None, end=False):
        self.childs:Dict[str, Optional[Node]] = childs if childs is not None else {}
        self.end=end

class WordDictionary:
    def __init__(self, node:Node=None):
        self.root = node if node is not None else Node()
        
    def addWord(self, word: str)->None:
        node = self.root
        for char in word:
            if char not in node.childs:
                node.childs[char] = Node()
            node = node.childs[char]
        node.end = True
    
    def search(self, word:str)->bool:
        stack = [(self.root, 0)]
        while stack:
            node, i = stack.pop()
            if i == len(word):
                if node.end:
                    return True
                continue
            char = word[i]
            if char == ".":
                for child in node.childs.values():
                    stack.append((child, i+1))
            else:
                if char in node.childs:
                    stack.append((node.childs[char],i+1))
        return False


class TestWordDictionary(unittest.TestCase):
    def setUp(self):
        self.wd = WordDictionary()
    
    def test_basic_add_and_search(self):
        self.wd.addWord("bad")
        self.wd.addWord("dad")
        self.wd.addWord("mad")
        
        self.assertFalse(self.wd.search("pad"))
        self.assertTrue(self.wd.search("bad"))
        self.assertTrue(self.wd.search(".ad"))
        self.assertTrue(self.wd.search("b.."))
    
    def test_wildcard_matching(self):
        self.wd.addWord("bad")
        self.wd.addWord("tax")
        
        self.assertTrue(self.wd.search(".ax"))
        self.assertTrue(self.wd.search("..."))
        self.assertTrue(self.wd.search("..x"))
        self.assertTrue(self.wd.search("b.d"))
        self.assertFalse(self.wd.search("..y"))
    
    def test_exact_match_only(self):
        self.wd.addWord("hello")
        self.wd.addWord("world")
        
        self.assertTrue(self.wd.search("hello"))
        self.assertTrue(self.wd.search("world"))
        self.assertFalse(self.wd.search("hell"))
        self.assertFalse(self.wd.search("worlds"))
        self.assertFalse(self.wd.search("hi"))
    
    def test_all_wildcards(self):
        self.wd.addWord("abc")
        self.wd.addWord("xyz")
        
        self.assertTrue(self.wd.search("..."))
        self.assertFalse(self.wd.search("...."))
        self.assertFalse(self.wd.search(".."))
    
    def test_prefix_not_matching(self):
        self.wd.addWord("apple")
        
        self.assertFalse(self.wd.search("app"))
        self.assertFalse(self.wd.search("appl"))
        self.assertTrue(self.wd.search("apple"))
    
    def test_mixed_wildcards(self):
        self.wd.addWord("cat")
        self.wd.addWord("car")
        self.wd.addWord("card")
        
        self.assertTrue(self.wd.search("ca."))
        self.assertTrue(self.wd.search(".ar"))
        self.assertTrue(self.wd.search("c..d"))
        self.assertFalse(self.wd.search("c.d"))
    
    def test_single_character(self):
        self.wd.addWord("a")
        self.wd.addWord("b")
        
        self.assertTrue(self.wd.search("a"))
        self.assertTrue(self.wd.search("."))
        self.assertFalse(self.wd.search("c"))
    
    def test_empty_dictionary(self):
        empty_wd = WordDictionary()
        self.assertFalse(empty_wd.search("test"))
        self.assertFalse(empty_wd.search("."))
    
    def test_duplicate_words(self):
        self.wd.addWord("test")
        self.wd.addWord("test")
        
        self.assertTrue(self.wd.search("test"))
        self.assertTrue(self.wd.search("...."))
    
    def test_multiple_branches_with_wildcard(self):
        self.wd.addWord("bad")
        self.wd.addWord("bed")
        self.wd.addWord("bid")
        self.wd.addWord("bod")
        self.wd.addWord("bud")
        
        self.assertTrue(self.wd.search("b.d"))
        self.assertFalse(self.wd.search("b.t"))
    
    def test_longer_words(self):
        self.wd.addWord("programming")
        self.wd.addWord("algorithm")
        
        self.assertTrue(self.wd.search("programming"))
        self.assertTrue(self.wd.search("...gramming"))
        self.assertTrue(self.wd.search("pro........"))
        self.assertTrue(self.wd.search(".lgorithm"))
        self.assertFalse(self.wd.search("program"))
    
    def test_similar_prefixes(self):
        self.wd.addWord("aa")
        self.wd.addWord("ab")
        self.wd.addWord("ba")
        self.wd.addWord("bb")
        
        self.assertTrue(self.wd.search(".."))
        self.assertTrue(self.wd.search("a."))
        self.assertTrue(self.wd.search(".b"))
        self.assertFalse(self.wd.search("c."))


if __name__ == "__main__":
    unittest.main()