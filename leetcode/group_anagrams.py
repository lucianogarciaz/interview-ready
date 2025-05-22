from typing import List, Dict
import unittest

"""
LeetCode Problem: Group Anagrams
Difficulty: Medium
Category: String, Hash Table, Sorting
Companies: Amazon, Microsoft, Bloomberg, Apple, Google

Problem Description:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 104
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

Time Complexity: O(n * k * log k) where n is the number of strings and k is the maximum length of a string
Space Complexity: O(n * k) where n is the number of strings and k is the maximum length of a string
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash: Dict[str, List[str]] = {}
        for s in strs:
            strSorted = ''.join(sorted(s))
            if strSorted in hash:
                hash[strSorted].append(s)
            else:
                hash[strSorted] = [s]

        return list(hash.values())

class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = self.solution.groupAnagrams(strs)
        # Sort both the outer and inner lists for consistent comparison
        result = [sorted(group) for group in sorted(result, key=lambda x: sorted(x)[0])]
        expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        expected = [sorted(group) for group in sorted(expected, key=lambda x: sorted(x)[0])]
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        strs = [""]
        expected = [[""]]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(result, expected)
    
    def test_example_3(self):
        strs = ["a"]
        expected = [["a"]]
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
