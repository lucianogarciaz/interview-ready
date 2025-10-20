from typing import Dict, List
import unittest

class Node:
    def __init__(self):
        self.childs:Dict[str, Node] = {}
        self.ended = False

class MagicDictionary:
    def __init__(self):
        self.root = Node()
        self.lengths = set()
    def buildDict(self, words:List[str])->None:
        for word in words:
            node = self.root
            self.lengths.add(len(word))
            for char in word:
                if char not in node.childs:
                    node.childs[char] = Node()
                node = node.childs[char]
            node.ended = True

    def search(self, word:str)->bool:
        if len(word) not in self.lengths:
            return False
        stack = [(self.root,0,False)]
        while stack:
            node, i, changed = stack.pop()
            if len(word)==i:
                if node.ended and changed:
                    return True
                continue
            char = word[i]
            if char in node.childs:
                stack.append((node.childs[char],i+1,changed))
            if not changed:
                for key, child in node.childs.items():
                    if key != char:
                        stack.append((child, i+1, True))

        return False


class TestMagicDictionary(unittest.TestCase):
    
    def test_basic_functionality(self):
        magic_dict = MagicDictionary()
        magic_dict.buildDict(["hello", "leetcode"])
        
        self.assertTrue(magic_dict.search("hallo"))
        self.assertTrue(magic_dict.search("heclo"))
        self.assertFalse(magic_dict.search("hell"))
        self.assertFalse(magic_dict.search("leetcoded"))
    
    def test_example_1(self):
        magic_dict = MagicDictionary()
        magic_dict.buildDict(["hello", "leetcode"])
        self.assertFalse(magic_dict.search("hello"))
        self.assertTrue(magic_dict.search("hhllo"))
        self.assertFalse(magic_dict.search("hell"))
        self.assertFalse(magic_dict.search("leetcoded"))
    
    def test_example_2(self):
        magic_dict = MagicDictionary()
        magic_dict.buildDict(["hello", "hallo", "leetcode"])
        self.assertTrue(magic_dict.search("hello"))
        self.assertTrue(magic_dict.search("hhllo"))
        self.assertFalse(magic_dict.search("hell"))
        self.assertFalse(magic_dict.search("leetcoded"))
    
    def test_single_character_word(self):
        magic_dict = MagicDictionary()
        magic_dict.buildDict(["a"])
        self.assertTrue(magic_dict.search("b"))
        self.assertTrue(magic_dict.search("z"))
        self.assertFalse(magic_dict.search("a"))
        self.assertFalse(magic_dict.search("ab"))
    
    def test_no_match_different_length(self):
        magic_dict = MagicDictionary()
        magic_dict.buildDict(["hello"])
        self.assertFalse(magic_dict.search("hi"))
        self.assertFalse(magic_dict.search("helloo"))
        self.assertFalse(magic_dict.search("helloworld"))
    
    def test_exact_match_should_fail(self):
        magic_dict = MagicDictionary()
        magic_dict.buildDict(["hello", "world"])
        self.assertFalse(magic_dict.search("hello"))
        self.assertFalse(magic_dict.search("world"))
    
    def test_one_character_difference(self):
        magic_dict = MagicDictionary()
        magic_dict.buildDict(["hello"])
        self.assertTrue(magic_dict.search("hallo"))
        self.assertTrue(magic_dict.search("hella"))
        self.assertTrue(magic_dict.search("xello"))
        self.assertTrue(magic_dict.search("hellx"))
    
    def test_multiple_words_same_length(self):
        magic_dict = MagicDictionary()
        magic_dict.buildDict(["cat", "bat", "rat"])
        self.assertTrue(magic_dict.search("cat"))
        self.assertTrue(magic_dict.search("bat"))
        self.assertTrue(magic_dict.search("rat"))
        self.assertTrue(magic_dict.search("hat"))
        self.assertFalse(magic_dict.search("dog"))
    
    def test_multiple_words_different_lengths(self):
        magic_dict = MagicDictionary()
        magic_dict.buildDict(["a", "ab", "abc", "abcd"])
        self.assertTrue(magic_dict.search("b"))
        self.assertTrue(magic_dict.search("bb"))
        self.assertTrue(magic_dict.search("bbc"))
        self.assertTrue(magic_dict.search("bbcd"))
        self.assertFalse(magic_dict.search("abcde"))
    
    def test_empty_dictionary(self):
        magic_dict = MagicDictionary()
        magic_dict.buildDict([])
        self.assertFalse(magic_dict.search("hello"))
        self.assertFalse(magic_dict.search("a"))
    
    def test_complex_words(self):
        magic_dict = MagicDictionary()
        magic_dict.buildDict(["programming", "algorithm", "datastructure"])
        self.assertTrue(magic_dict.search("pxogramming"))
        self.assertTrue(magic_dict.search("algoxithm"))
        self.assertTrue(magic_dict.search("datastructurx"))
        self.assertFalse(magic_dict.search("programming"))
        self.assertFalse(magic_dict.search("algorithm"))
        self.assertFalse(magic_dict.search("datastructure"))
    
    def test_all_positions_changed(self):
        magic_dict = MagicDictionary()
        magic_dict.buildDict(["abc"])
        self.assertTrue(magic_dict.search("xbc"))
        self.assertTrue(magic_dict.search("axc"))
        self.assertTrue(magic_dict.search("abx"))
        self.assertFalse(magic_dict.search("xyz"))
    
    def test_similar_words_with_prefix(self):
        magic_dict = MagicDictionary()
        magic_dict.buildDict(["test", "testing", "tester"])
        self.assertTrue(magic_dict.search("best"))
        self.assertTrue(magic_dict.search("testxng"))
        self.assertTrue(magic_dict.search("testex"))
        self.assertFalse(magic_dict.search("test"))
        self.assertFalse(magic_dict.search("testing"))
    
    def test_two_character_words(self):
        magic_dict = MagicDictionary()
        magic_dict.buildDict(["ab", "cd", "ef"])
        self.assertFalse(magic_dict.search("ab"))
        self.assertTrue(magic_dict.search("ax"))
        self.assertTrue(magic_dict.search("xd"))
        self.assertTrue(magic_dict.search("cb"))
        self.assertFalse(magic_dict.search("xy"))
        self.assertFalse(magic_dict.search("gh"))


if __name__ == '__main__':
    unittest.main()