from typing import List
import unittest

"""
LeetCode Problem: Valid Anagram
Difficulty: Easy
Category: String, Hash Table, Sorting
Companies: Amazon, Microsoft, Bloomberg, Apple, Google

Problem Description:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 104
- s and t consist of lowercase English letters.

Follow-up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

Time Complexity Solutions:
1. Sorting: O(n log n) where n is the length of the string
2. Hash Table: O(n) where n is the length of the string

Space Complexity Solutions:
1. Sorting: O(1) if we use in-place sorting
2. Hash Table: O(k) where k is the size of the character set
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        hashS = {}
        hashT = {}
        for a in s:
            if a in hashS:
                hashS[a] += 1
            else:
                hashS[a] = 1

        for a in t:
            if a in hashT:
                hashT[a] +=1
            else:
                hashT[a] = 1

        return hashT == hashS

class TestValidAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        s = "anagram"
        t = "nagaram"
        expected = True
        result = self.solution.isAnagram(s, t)
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        s = "rat"
        t = "car"
        expected = False
        result = self.solution.isAnagram(s, t)
        self.assertEqual(result, expected)
    
    def test_empty_strings(self):
        s = ""
        t = ""
        expected = True
        result = self.solution.isAnagram(s, t)
        self.assertEqual(result, expected)
    
    def test_different_lengths(self):
        s = "hello"
        t = "world"
        expected = False
        result = self.solution.isAnagram(s, t)
        self.assertEqual(result, expected)
    
    def test_same_string(self):
        s = "python"
        t = "python"
        expected = True
        result = self.solution.isAnagram(s, t)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main() 